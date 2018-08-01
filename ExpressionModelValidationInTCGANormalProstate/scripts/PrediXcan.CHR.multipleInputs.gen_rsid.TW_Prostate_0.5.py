#!/usr/bin/env python

import argparse
from collections import defaultdict
import datetime
import gzip
import numpy as np
import os
import sqlite3
import sys
import subprocess
import pickle as pkl

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

# e.g.
# 17 17:30038360_A_C rs552816285 30038360 A C 1.00000 0.00000 0.00000 1.00000 0.00000 0.00000 1.00000 0.00000 0.0000
# 17 17:30038416_AG_A 17:30038416_AG_A 30038416 AG A 1.00000 0.00000 0.00000 1.00000 0.00000 0.00000 1.00000 0.00000
def get_all_dosages(dosage_dir, dosage_prefix, dbuffer=None):
    for chrfile in [x for x in sorted(os.listdir(dosage_dir)) if x.startswith(dosage_prefix) and x.endswith(".gen.gz")]:
        print datetime.datetime.now(), "Processing %s" % chrfile
        for line in buffered_file(gzip.open(os.path.join(dosage_dir, chrfile)), dosage_buffer=dbuffer):
            arr = line.strip().split()
            chr = arr[0]
            snpid = arr[1]
            rsid = arr[2]
            pos = arr[3]
            altallele = arr[5]
            refallele = arr[6]
            dosage_row = np.array(arr[7:], dtype=np.float64)
            yield chr, snpid, rsid, pos, altallele, refallele, dosage_row


def RevComp(allele):
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


def GetChromosomesByGene():
  db = WeightsDB(beta_file)
  for tup in db.query("SELECT DISTINCT trim(substr(rsid,4,2),'.') || '#SEP#' || gene  from weights"):
    self.tuples[tup[0]].append(tup[1:])


def GetGenesByChromosome(beta_file, target_chr):

  with open("../dbs/prostate_chrdb.pkl","r") as infh:
    chrdb = pkl.load(infh)

  conn = sqlite3.connect("../dbs/TW_Prostate_0.5.db")
  c = conn.cursor()
  c.execute("SELECT gene, genename FROM extra")
  results = c.fetchall()
  ensgenes = [str(x[0]).split(".")[0] for x in results]
  common_name_map = {str(x[0]).split(".")[0]:str(x[1]) for x in results}

  # db = WeightsDB(beta_file)
  # geneChrTuples = []
  # for tup in db.query("SELECT DISTINCT trim(substr(rsid,4,2),'.') || '#SEP#' || gene from weights"):
  #   geneChrTuples.append(tup)
  # targetChromosomeGenes = [str(x[0]).split("#SEP#")[1] for x in geneChrTuples if str(x[0]).split("#SEP#")[0] == target_chr]

  targetChromosomeGenes = [ensgene for ensgene in ensgenes if chrdb[ensgene] == target_chr]
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
    def __init__(self, beta_file, sample_file, chromosome=None):
        self.D = None
        self.beta_file = beta_file
        self.chromosome = chromosome
        self.sample_file = sample_file
        # self.complements = {"A":"T","C":"G","G":"C","T":"A"}
        self.gene_list, self.gene_common_name_map = [], {}

    def get_gene_list(self):
        targetChromosomeGenes, common_name_map = GetGenesByChromosome(self.beta_file, self.chromosome)
        gene_list = sorted(targetChromosomeGenes)
        print "Length of gene list", len(gene_list)
        return(gene_list, common_name_map)

    def update(self, gene, weight, ref_allele, alt_allele, allele, altallele, dosage_row, rsid):
        if self.D is None:
            self.gene_list, self.gene_common_name_map = self.get_gene_list()
            self.gene_index = { gene:k for (k, gene) in enumerate(self.gene_list) }
            self.D = np.zeros((len(self.gene_list), len(dosage_row))) # Genes x Cases
        if gene in self.gene_index: #assumes strands are aligned to PrediXcan reference and dosage coding 0 to 2
            # if alt_allele == self.complements[ref_allele]:
            if alt_allele == RevComp(ref_allele):
                # print "Ambiguous SNP: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
                pass
            elif ref_allele == allele and alt_allele == altallele:
                self.D[self.gene_index[gene],] += dosage_row * weight
                # print "Match Type 1: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
            # elif ref_allele == self.complements[allele] and alt_allele == self.complements[altallele]:
            elif ref_allele == RevComp(allele) and alt_allele == RevComp(altallele):
                self.D[self.gene_index[gene],] += dosage_row * weight
                # print "Match Type 2: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
            elif ref_allele == altallele and alt_allele == allele:
                self.D[self.gene_index[gene],] += (2-dosage_row) * weight # Update all cases for that gene
                # print "Match Type 3: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
            # elif ref_allele == self.complements[altallele] and alt_allele == self.complements[allele]:
            elif ref_allele == RevComp(altallele) and alt_allele == RevComp(allele):
                self.D[self.gene_index[gene],] += (2-dosage_row) * weight # Update all cases for that gene
                # print "Match Type 4: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
            else:
                # print "Match Type 5: "+"\t".join(["gene :"+gene,"rsid: "+rsid,"DB Ref: "+alt_allele,"User Ref: "+altallele,"DB Eff: "+ref_allele,"User Eff: "+allele])
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
    parser.add_argument('--assoc', action="store_true", dest="assoc", default=False, help="Include to perform association test")
    parser.add_argument('--genelist', action="store", dest="genelist", default=None, help="Text file with chromosome, gene pairs.")
    parser.add_argument('--chromosome', action="store", dest="chromosome", default="data/dosages", help="Target chromosome.")
    parser.add_argument('--dosages', action="store", dest="dosages", default="data/dosages", help="Path to a directory of gzipped dosage files.")
    parser.add_argument('--dosages_prefix', dest="dosages_prefix", default="chr", action="store", help="Prefix of filenames of gzipped dosage files.")
    parser.add_argument('--dosages_buffer', dest="dosages_buffer", default=None, action="store", help="Buffer size in GB for each dosage file (default: read line by line)")
    parser.add_argument('--samples', dest='sample_file', default="samples.txt", action="store", help="File in dosages directory with individual ids.  Must be in same order as columns for dosages")
    parser.add_argument('--weights', action="store", dest="weights",default="data/weights.db", help="SQLite database with rsid weights.")
    parser.add_argument('--weights_on_disk', action="store_true", dest="weights_on_disk", help="Don't load weights db to memory.")
    parser.add_argument('--pheno', action="store", dest="pheno", default=None, help="Phenotype file")
    parser.add_argument('--mpheno', action="store", dest="mpheno", default=None, help="Specify which phenotype column if > 1")
    parser.add_argument('--pheno_name', action="store", dest="pheno_name", default=None, help="Column name of the phenotype to perform association on.")
    parser.add_argument('--missing-phenotype', action="store", dest="missing_phenotype",  default='NA', help="Specify code for missing phenotype information.  Default is NA")
    parser.add_argument('--filter', nargs=2, action="store", dest="fil", default=None, help="Takes two arguments. First is the name of the filter file, the second is a value to filter on.")
    parser.add_argument('--mfilter', action="store", dest="mfil", default=None, help="Column number of filter file to filter on.  '1' specifies the first filter column")
    parser.add_argument('--output_dir', action="store", dest="output", default="output", help="Path to output directory")
    parser.add_argument('--pred_exp', action="store", dest="pred_exp", default=None, help="Predicted expression file from earlier run of PrediXcan")
    parser.add_argument('--logistic', action="store_true", dest="logistic", default=False, help="Include to perform a logistic regression")
    parser.add_argument('--linear', action="store_true", dest="linear", default=False, help="Include to perform a linear regression")
    parser.add_argument('--survival', action="store_true", dest="survival", default=False, help="Include to perform survival analysis")

    args = parser.parse_args()

    PREDICT = args.predict
    CHROMOSOME = args.chromosome
    DOSAGE_DIR = args.dosages
    DOSAGE_PREFIX = args.dosages_prefix
    DOSAGE_BUFFER = int(args.dosages_buffer) if args.dosages_buffer else None
    SAMPLE_FILE = os.path.join(DOSAGE_DIR, args.sample_file)
    BETA_FILE = args.weights
    PRELOAD_WEIGHTS = not args.weights_on_disk
    ASSOC = args.assoc
    PHENO_FILE = args.pheno
    MPHENO = str(int(args.mpheno) + 2) if args.mpheno else 'None'
    PHENO_NAME = args.pheno_name if args.pheno_name else 'None'
    MISSING_PHENOTYPE = args.missing_phenotype
    FILTER_FILE, FILTER_VAL = args.fil if args.fil else ('None', '1')
    MFILTER = args.mfil if args.mfil else 'None'
    OUTPUT_DIR = args.output
    PRED_EXP_FILE = args.pred_exp if args.pred_exp else os.path.join(OUTPUT_DIR, "predicted_expression.txt")
    ASSOC_FILE = os.path.join(OUTPUT_DIR, "association.txt")
    if args.logistic:
        TEST_TYPE = "logistic"
    elif args.survival:
        TEST_TYPE = "survival"
    else:
        TEST_TYPE = "linear"

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    if os.path.exists(PRED_EXP_FILE) and PREDICT:
        print PRED_EXP_FILE + ' already exists! Move or change this filename to run this prediction.'
    if not os.path.exists(PRED_EXP_FILE) and PREDICT:
        get_applications_of = GetApplicationsOf(BETA_FILE, PRELOAD_WEIGHTS)
        transcription_matrix = TranscriptionMatrix(BETA_FILE, SAMPLE_FILE, CHROMOSOME)
        #          get_all_dosages fxn                      
        # yield rsid, refallele, altallele, dosage_row --> rsid, allele, altallele,dosage_row
        # so refallele --> allele, and altallele --> altallele
        # now,
        # yield chr, snpid, rsid, pos, altallele, refallele, dosage_row --> chr, snpid, rsid, pos, altallele, refallele, dosage_row
        # so should be chr, snpid, rsid, pos, altallele, allele, dosage_row
        for chr, snpid, rsid, pos, altallele, refallele, dosage_row in get_all_dosages(DOSAGE_DIR, DOSAGE_PREFIX, DOSAGE_BUFFER):
            for gene, weight, ref_allele, alt_allele in get_applications_of(rsid):
                print "Updating for %s, %s" % (gene, rsid)
                transcription_matrix.update(gene, weight, ref_allele, alt_allele, refallele, altallele, dosage_row, rsid)
        transcription_matrix.save(PRED_EXP_FILE)
    if ASSOC:
        subprocess.call(
            ["./PrediXcanAssociation.R",
            "PRED_EXP_FILE", PRED_EXP_FILE,
            "PHENO_FILE", PHENO_FILE,
            "PHENO_COLUMN", MPHENO,
            "PHENO_NAME", PHENO_NAME,
            "MISSING_PHENOTYPE", MISSING_PHENOTYPE,
            "FILTER_FILE", FILTER_FILE,
            "FILTER_VAL", FILTER_VAL,
            "FILTER_COLUMN", MFILTER,
            "TEST_TYPE", TEST_TYPE,
            "OUT", ASSOC_FILE])


if __name__ == '__main__':
    main()
