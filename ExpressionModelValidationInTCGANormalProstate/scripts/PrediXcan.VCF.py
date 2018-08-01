#!/usr/bin/env python

from collections import defaultdict
import argparse, datetime, gzip, numpy as np, os, pickle as pkl, re, sqlite3, sys, subprocess

def buffered_file(file, dosage_buffer=None):
    if not dosage_buffer:
        for line in file:
            yield line
    else:
        buf = ''
        while True:
            buf = buf + file.read(dosage_buffer*(1024**3))
            if not buf:
                raise StopIteration
            last_eol = 0
            while True:
                next_eol = buf.find('\n', last_eol)
                if next_eol == -1: # No end of line here.
                    buf = buf[last_eol:]
                    break # keep the last fragment, read the next chunk
                else:
                    yield buf[last_eol:next_eol+1]
                    last_eol = next_eol + 1
                    if last_eol >= len(buf):
                        buf = ''
                        break

# VCF Format: https://samtools.github.io/hts-specs/VCFv4.2.pdf
def get_all_dosages(dosage_dir, dosage_prefix, use_rsid, dbuffer=None):
    for input_file in [x for x in sorted(os.listdir(dosage_dir)) if x.startswith(dosage_prefix) and x.endswith(".vcf.gz")]:
        print datetime.datetime.now(), "Processing %s" % input_file
        for line in buffered_file(gzip.open(os.path.join(dosage_dir, input_file)), dosage_buffer=dbuffer):
            if line[:2] == "##":
              continue
            elif line[0] == "#":
              header_fields = line[1:].strip().split()
              try:
                assert header_check(header_fields)
              except Exception as caught:
                print "Exception raised: VCF header incorrectly formatted (see https://samtools.github.io/hts-specs/VCFv4.2.pdf)"
                print caught
                sys.exit(1)
            else:
              vcf_fields = line.strip().split()
              (chr, pos, snpid, ref_allele, alt_allele, qual, filter, info, format) = tuple(vcf_fields[:9])
              dosage_index = format.split(":").index("DS")
              dosage_values = np.array([gt_string.split(":")[dosage_index] for gt_string in vcf_fields[9:]], dtype=np.float64)
              if use_rsid:
                rsid = snpid
              else:
                rsid = ".".join(["chr"+chr, pos, ref_allele, alt_allele])
              yield chr, snpid, rsid, pos, ref_allele, alt_allele, dosage_values


def header_check(header_fields):
  chrom_flag  = header_fields[0] == "CHROM"
  pos_flag    = header_fields[1] == "POS"
  id_flag     = header_fields[2] == "ID"
  ref_flag    = header_fields[3] == "REF"
  alt_flag    = header_fields[4] == "ALT"
  qual_flag   = header_fields[5] == "QUAL"
  filter_flag = header_fields[6] == "FILTER"
  info_flag   = header_fields[7] == "INFO"
  format_flag = header_fields[8] == "FORMAT"
  return (chrom_flag and pos_flag and id_flag and ref_flag and \
          alt_flag and qual_flag and filter_flag and info_flag and format_flag)


def revComp(allele):
  revDict = {"A":"T","C":"G","G":"C","T":"A","-":"-"}
  return "".join([revDict[allele[i].upper()] for i in range(len(allele)-1,-1,-1)])


class WeightsDB:
    def __init__(self, beta_file):
        self.conn = sqlite3.connect(beta_file)

    def query(self, sql, args=None):
        c = self.conn.cursor()
        if args:
            for ret in c.execute(sql, args):
                yield ret
        else:
            for ret in c.execute(sql):
                yield ret


def get_chromosomes_by_gene():
  db = WeightsDB(beta_file)
  for tup in db.query("SELECT DISTINCT trim(substr(rsid,4,2),'.') || '#SEP#' || gene  from weights"):
    self.tuples[tup[0]].append(tup[1:])


def get_genes_by_chromosome(beta_file, target_chr, use_rsid):
  if use_rsid:
    with open("prostate_chrdb.pkl","r") as infh:
      chrdb = pkl.load(infh)

    conn = sqlite3.connect(beta_file)
    c = conn.cursor()
    c.execute("SELECT gene, genename FROM extra")
    results = c.fetchall()
    ensgenes = [str(x[0]).split(".")[0] for x in results]
    common_name_map = {str(x[0]).split(".")[0]:str(x[1]) for x in results}
    targetChromosomeGenes = [ensgene for ensgene in ensgenes if ensgene in chrdb and str(chrdb[ensgene]) == target_chr]
  else:
    db = WeightsDB(beta_file)
    geneChrTuples = []
    for tup in db.query("SELECT DISTINCT trim(substr(rsid,4,2),'.') || '#SEP#' || gene from weights"):
      geneChrTuples.append(tup)
    targetChromosomeGenes = [str(x[0]).split("#SEP#")[1] for x in geneChrTuples if str(x[0]).split("#SEP#")[0] == target_chr]
    common_name_map = {geneName:geneName for geneName in targetChromosomeGenes}

  return targetChromosomeGenes, common_name_map


class GetApplicationsOf:
    def __init__(self, beta_file, preload_weights=True):
        self.db = WeightsDB(beta_file)
        if preload_weights:
            print datetime.datetime.now(), "Preloading weights..."
            self.tuples = defaultdict(list)
            for tup in self.db.query("SELECT rsid, gene, weight, eff_allele, ref_allele FROM weights"):
                self.tuples[tup[0]].append(tup[1:])
        else:
            self.tuples = None

    def __call__(self, rsid):
        if self.tuples:
            for tup in self.tuples[rsid]:
                yield tup
        else:
            for tup in self.db.query("SELECT gene, weight, eff_allele, ref_allele, FROM weights WHERE rsid=?", (rsid,)):
                yield tup


class TranscriptionMatrix:
    def __init__(self, beta_file, sample_file, use_rsid, chromosome=None):
        self.D = None
        self.beta_file = beta_file
        self.chromosome = chromosome
        self.use_rsid = use_rsid
        self.sample_file = sample_file
        # self.complements = {"A":"T","C":"G","G":"C","T":"A"}
        self.gene_list, self.gene_common_name_map = [], {}

    def get_gene_list(self):
        targetChromosomeGenes, common_name_map = get_genes_by_chromosome(self.beta_file, self.chromosome, self.use_rsid)
        gene_list = sorted(targetChromosomeGenes)
        return(gene_list, common_name_map)

    # gene, weight, db_ref, db_alt, input_ref, input_alt, dosage_row, rsid
    def update(self, gene, weight, db_ref, db_alt, input_ref, input_alt, dosage_row, rsid):
        if self.D is None:
            self.gene_list, self.gene_common_name_map = self.get_gene_list()
            self.gene_index = { gene:k for (k, gene) in enumerate(self.gene_list) }
            self.D = np.zeros((len(self.gene_list), len(dosage_row))) # Genes x Cases
        if gene in self.gene_index: #assumes strands are aligned to PrediXcan reference and dosage coding 0 to 2
            if db_alt == revComp(db_ref):
                print "Ambiguous SNP: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
                pass
            elif db_ref == input_ref and db_alt == input_alt:
                self.D[self.gene_index[gene],] += dosage_row * weight
                print "Match Type 1: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
            elif db_ref == revComp(input_ref) and db_alt == revComp(input_alt):
                self.D[self.gene_index[gene],] += dosage_row * weight
                print "Match Type 2: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
            elif db_ref == input_alt and db_alt == input_ref:
                self.D[self.gene_index[gene],] += (2-dosage_row) * weight # Update all cases for that gene
                print "Match Type 3: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
            elif db_ref == revComp(input_alt) and db_alt == revComp(input_ref):
                self.D[self.gene_index[gene],] += (2-dosage_row) * weight # Update all cases for that gene
                print "Match Type 4: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
            else:
                print "Match Type 5: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+db_alt,"User Ref: "+input_alt,"DB Eff: "+db_ref,"User Eff: "+input_ref])
                pass

    def get_samples(self):
        with open(self.sample_file, 'r') as samples:
            for line in samples:
                yield [line.split()[0], line.split()[1]]
                    
    def save(self, pred_exp_file):
        sample_generator = self.get_samples()
        with open(pred_exp_file, 'w+') as outfile:
            common_gene_names_in_order = [self.gene_common_name_map[ens_gene] for ens_gene in self.gene_list]
            outfile.write('FID\t' + 'IID\t' + '\t'.join(common_gene_names_in_order) + '\n') # Nb. this lists the names of rows, not of columns
            for col in range(0, self.D.shape[1]):
                try:
                    outfile.write('\t'.join(next(sample_generator)) + '\t' + '\t'.join(map(str, self.D[:,col]))+'\n')
                except StopIteration:
                    print "ERROR: There are not enough rows in your sample file!"
                    print "Make sure dosage files and sample files have the same number of individuals in the same order."
                    os.remove(pred_exp_file)
                    sys.exit(1)
            try:
                next(sample_generator)
            except StopIteration:
                print "Predicted expression file complete!"
            else:
                print "ERROR: There are too many rows in your sample file!"
                print "Make sure dosage files and sample files have the same number of individuals in the ame order."
                os.remove(pred_exp_file)
                sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predict', action="store_true", dest="predict", default=False, help="Include to predict gene expression")
    parser.add_argument('--genelist', action="store", dest="genelist", default=None, help="Text file with chromosome, gene pairs.")
    parser.add_argument('--chromosome', action="store", dest="chromosome", default="data/dosages", help="Integer number of chromosome to be queried / imputed.")
    parser.add_argument('--dosages', action="store", dest="dosages", default="data/dosages", help="Path to a directory of gzipped dosage files.")
    parser.add_argument('--dosages_prefix', dest="dosages_prefix", default="chr", action="store", help="Prefix of filenames of gzipped dosage files.")
    parser.add_argument('--dosages_buffer', dest="dosages_buffer", default=None, action="store", help="Buffer size in GB for each dosage file (default: read line by line)")
    parser.add_argument('--samples', dest='sample_file', default="samples.txt", action="store", help="File in dosages directory with individual ids.  Must be in same order as columns for dosages")
    parser.add_argument('--weights', action="store", dest="weights",default="data/weights.db", help="SQLite database with rsid weights.")
    parser.add_argument('--weights_on_disk', action="store_true", dest="weights_on_disk", help="Don't load weights db to memory.")
    parser.add_argument('--output_dir', action="store", dest="output", default="output", help="Path to output directory")
    parser.add_argument('--pred_exp', action="store", dest="pred_exp", default=None, help="Predicted expression file from earlier run of PrediXcan")
    parser.add_argument('--use_rsid', action="store_true", dest="use_rsid", default=None, help="Use VCF ID column, containing dbSNP rsid, for SNP ID's. Otherwise, use combination of chromosome, position and alleles")

    args = parser.parse_args()

    PREDICT = args.predict
    CHROMOSOME = args.chromosome
    DOSAGE_DIR = args.dosages
    DOSAGE_PREFIX = args.dosages_prefix
    DOSAGE_BUFFER = int(args.dosages_buffer) if args.dosages_buffer else None
    SAMPLE_FILE = os.path.join(DOSAGE_DIR, args.sample_file)
    BETA_FILE = args.weights
    PRELOAD_WEIGHTS = not args.weights_on_disk
    OUTPUT_DIR = args.output
    PRED_EXP_FILE = args.pred_exp if args.pred_exp else os.path.join(OUTPUT_DIR, "predicted_expression.txt")
    USE_RSID = args.use_rsid

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    if os.path.exists(PRED_EXP_FILE) and PREDICT:
        print PRED_EXP_FILE + ' already exists! Move or change this filename to run this prediction.'
    if not os.path.exists(PRED_EXP_FILE) and PREDICT:
        get_applications_of = GetApplicationsOf(BETA_FILE, PRELOAD_WEIGHTS)
        transcription_matrix = TranscriptionMatrix(BETA_FILE, SAMPLE_FILE, USE_RSID, CHROMOSOME)
        #          get_all_dosages fxn                      
        # yield rsid, refallele, altallele, dosage_row --> rsid, allele, altallele,dosage_row
        # so refallele --> allele, and altallele --> altallele
        # now,
        # yield chr, snpid, rsid, pos, altallele, refallele, dosage_row --> chr, snpid, rsid, pos, altallele, refallele, dosage_row
        # so should be chr, snpid, rsid, pos, altallele, allele, dosage_row
        for chr, snpid, rsid, pos, input_ref, input_alt, dosage_row in get_all_dosages(DOSAGE_DIR, DOSAGE_PREFIX, USE_RSID, DOSAGE_BUFFER):
            for gene, weight, db_alt, db_ref in get_applications_of(rsid):
                ensembl_match = re.search("(ENSG[\d]+)\.[\d]+", gene)
                if ensembl_match:
                  gene = ensembl_match.group(1)
                print "Updating for %s, %s" % (gene, rsid)
                transcription_matrix.update(gene, weight, db_ref, db_alt, input_ref, input_alt, dosage_row, rsid)
        transcription_matrix.save(PRED_EXP_FILE)

if __name__ == '__main__':
    main()
