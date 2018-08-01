import argparse, gzip, itertools, numpy, os, random, sqlite3, sys

def main(db_file, query_file, ref_file, path_to_bed_files, num_null):
  
  db_cxn, db_cur, h3k27ac_bed_list = create_sqlite_database(db_file, path_to_bed_files)
  query_tallies                    = intersect_query_regions_with_bed_peaks(db_cur, query_file, h3k27ac_bed_list)
  null_tally_distribution          = generate_null_distribution_of_tallies(db_cur, ref_file, h3k27ac_bed_list, num_null)
  
  print "** Final Results of Overlap Between Inputs and BED ChIP-Seq Peaks **"
  print "  Query Tallies Mean (SD = Stdev, N = Sample Size):", numpy.mean(query_tallies.values()), \
        "(SD = {stdev}, N = {smpsze})".format(stdev=numpy.std(query_tallies.values()), \
                                              smpsze = len(query_tallies.values()))
  print "  Null Tallies Mean (SD = Stdev, N = Sample Size):", numpy.mean(null_tally_distribution.values()), \
        "(SD = {stdev}, N = {smpsze})".format(stdev=numpy.std(null_tally_distribution.values()), \
                                              smpsze = len(null_tally_distribution.values()))
  
  db_cxn.close()


# create_sqlite_database: generate database of h3k27ac ChIP-Seq peaks
# Inputs: (optional) db filename, (optional) path to ICGC h3k27ac BED files
# Outputs: db connection object, db cursor object, list of sample names
def create_sqlite_database(db_file, path_to_bed_files):
  # Use user-provided SQLite DB of ICGC BED Intervals
  if db_file:
    db_cxn = sqlite3.connect(db_file)
    db_cur = db_cxn.cursor()
  
    db_cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    h3k27ac_bed_list = [output_tuple[0] for output_tuple in db_cur.fetchall()]
  # Or, create new SQLite DB of ICGC BED Intervals
  else:
    db_cxn = sqlite3.connect('h3k27ac.db')
    print "** NOTE: Created Database at ./h3k27ac.db **"
    db_cur = db_cxn.cursor()
  
    # Iterate through BED files to populate database
    h3k27ac_bed_list = []
    for bedfile in [bedfile for bedfile in os.listdir(path_to_bed_files) if bedfile[-4:] == ".bed"]:
      bed_table_name = bedfile[:-4]
      h3k27ac_bed_list.append(bed_table_name)
      h3k27ac_row_tuples = []
      with open(bedfile,"r") as infh:
        for line in infh:
          elements = line.strip().split()
          # Exclude non-autosomal chromosomes
          if "_" in elements[0] or "X" in elements[0] or "Y" in elements[0]:
            continue
          # Remove "chr" prefix (characters 1-3 of element 0)
          row_tuple = (int(elements[0][3:]), int(elements[1]), int(elements[2]))
          h3k27ac_row_tuples.append(row_tuple)
        create_sqlite_table(db_cxn, db_cur, bed_table_name, h3k27ac_row_tuples)

  return db_cxn, db_cur, h3k27ac_bed_list
  

# create_sqlite_table: generate single table of h3k27ac ChIP-Seq peaks
# Inputs: db connection object, db cursor object, table name, values to be populated
# Outputs: returns 1 if successful
def create_sqlite_table(db_cxn, db_cur, table_name, row_tuples):
  print "  Creating table: {tbl_name}".format(tbl_name=table_name)
  db_cur.execute('CREATE TABLE {tbl_name} (chromosome INTEGER, start INTEGER, stop INTEGER)'.format(tbl_name=table_name))
  db_cur.execute('CREATE INDEX {idx_name} ON {tbl_name} (chromosome)'.format(tbl_name=table_name, idx_name=table_name+"_chr_index"))
  db_cur.execute('CREATE INDEX {idx_name} ON {tbl_name} (start)'.format(tbl_name=table_name, idx_name=table_name+"_start_index"))
  db_cur.execute('CREATE INDEX {idx_name} ON {tbl_name} (stop)'.format(tbl_name=table_name, idx_name=table_name+"_stop_index"))

  db_cur.executemany('INSERT INTO {} VALUES (?,?,?)'.format(table_name), row_tuples)
  db_cxn.commit()
  return 1


# query_sqlite_table: Query sqlite table to see if input region overlaps with populated
#                     BED intervals from ICGC ChIP-Seq data
# Inputs: db cursor object, table name, values for query
# Outputs: output tuple from sqlite SELECT query
def query_sqlite_table(db_cur, table_name, query_tuple):
  db_cur.execute('SELECT * FROM {tbl_name} WHERE chromosome = ? AND ? >= start and ? <= stop'.format(tbl_name=table_name), query_tuple)
  output = db_cur.fetchone()
  return output


# intersect_query_regions_with_bed_peaks: tally the number of ChIP-Seq samples
#                                         with peaks that colocalize with a number
#                                         of input regions of SNP positions
# Inputs: db cursor, input file of query regions ("chr21:42893757"), list of db table names
# Outputs: dictionary mapping query region name to tally of samples with colocalized peaks
def intersect_query_regions_with_bed_peaks(db_cur, query_file, h3k27ac_bed_list):
  query_tallies = {}
  print "** Tallies of Input Overlap with BED ChIP-Seq Peaks **"
  with open(query_file,"r") as infh:
    with open(query_file+".output.txt","a") as outfh:
      for line in infh:
        query_snp = line.strip()
        query_chr = query_snp.split(":")[0][3:]
        query_pos = int(query_snp.split(":")[1])
        
        query_tally = 0
        for h3k27ac_bed_table in h3k27ac_bed_list:
          query_tally += 1 if query_sqlite_table(db_cur, h3k27ac_bed_table, (query_chr, query_pos, query_pos)) else 0
        
        query_tallies[query_snp] = query_tally
        print "  Input (Tally):", query_snp, "({qry_tally})".format(qry_tally = query_tally)
        outfh.write("\t".join([query_snp, str(query_tally)])+"\n")

  return query_tallies


# generate_null_distribution_of_tallies: generate database of h3k27ac ChIP-Seq peaks
# Inputs: (optional) db filename, (optional) path to ICGC h3k27ac BED files
# Outputs: database connection object, database cursor object, list of sample names
def generate_null_distribution_of_tallies(db_cur, ref_file, h3k27ac_bed_list, num_null):
  if ref_file:
    hrc_coordinate_list = generate_list_of_hrc_chr_and_pos(ref_file)
  
  null_tally_distribution = {}
  while(len(null_tally_distribution.values()) < num_null):
    if ref_file:
      random_hrc_sample = hrc_coordinate_list[int(random.random() * len(hrc_coordinate_list))]
      if "_" in random_hrc_sample[0] or "X" in random_hrc_sample[0] or "Y" in random_hrc_sample[0]:
        continue
      test_chr = int(random_hrc_sample[0])
      test_pos = int(random_hrc_sample[1])
    else:
      test_chr = generate_random_autosome()
      test_pos = generate_random_base_position(test_chr)
    
    null_tally = 0
    for h3k27ac_bed_table in h3k27ac_bed_list:
      null_tally += 1 if query_sqlite_table(db_cur, h3k27ac_bed_table, (test_chr, test_pos, test_pos)) else 0
    null_tally_distribution[":".join([str(test_chr), str(test_pos)])] = null_tally
  
  with open("Null_distribution_tallies.output","a") as outfh:
    for key, value in null_tally_distribution.iteritems():
      outfh.write("\t".join([str(key), str(value)])+"\n")

  return null_tally_distribution


# generate_random_autosome: generate random autosome number
# Inputs: none
# Outputs: integer between 1 and 22
def generate_random_autosome():
  return int(random.random() * 22.0) + 1


# generate_random_base_position: generate random autosome base position
# Inputs: chromosome number
# Outputs: integer between 1 and chromosome length
def generate_random_base_position(chr):
  autosome_lengths = {1: 249250621, 2: 243199373, 3: 198022430, 4: 191154276, 5: 180915260, 6: 171115067, 7: 159138663, 8: 146364022, 9: 141213431, 10: 135534747, 11: 135006516, 12: 133851895, 13: 115169878, 14: 107349540, 15: 102531392, 16: 90354753, 17: 81195210, 18: 78077248, 20: 63025520, 19: 59128983, 22: 51304566, 21: 48129895}
  return int(random.random() * autosome_lengths[chr]) + 1


# generate_list_of_hrc_chr_and_pos: slurp in all hrc reference panel chr's and pos's
# Inputs: HRC site list HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz
# Outputs: list of HRC coordinates
def generate_list_of_hrc_chr_and_pos(ref_file):
  hrc_coordinate_list = []
  spinner = itertools.cycle(['-', '/', '|', '\\'])
  counter = 0
  print "Processing HRC Reference Site List...  \\",
  with gzip.open(ref_file, 'rb') as gzfh:
    for line in gzfh:
      counter += 1
      if counter % 1e5 == 0:
        sys.stdout.flush()
        sys.stdout.write('\b%s' % spinner.next())
      chr_pos_list = line.strip().split()[:2]
      hrc_coordinate_list.append(tuple(chr_pos_list))
  sys.stdout.flush()
  sys.stdout.write("\bDone.\n")
  return hrc_coordinate_list


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='SNP vs. ChIP-Seq Peak Enrichment.')
  parser.add_argument('--db',  type=str, required=False, \
                      help='Name of (optional) input database of h3k27ac bed tables')
  parser.add_argument('--snp', type=str, required=True, \
                      help='Query File of SNP positions in format "chr21:42893757", for example.')
  parser.add_argument('--ref', type=str, required=False, \
                      help='Path to tabix indexed HRC site list HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz(.tbi)')
  parser.add_argument('--bed', type=str, required=False, \
                      help='''Path to input bed files if ICGC H3K27ac ChIP-Seq peak
                              BED files from GSE96652 (default: current directory).''', default="./")
  parser.add_argument('--num', type=int, required=True, \
                      help='Number of variants from reference to consider in null distribution.')

  args = parser.parse_args()
  main(args.db, args.snp, args.ref, args.bed, args.num)
