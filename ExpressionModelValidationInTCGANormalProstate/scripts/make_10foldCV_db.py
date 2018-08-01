import glob
import sqlite3
import sys

def Main():
  dbName = '../dbs/Prostate_Thibodeau.10foldCV.db'

  conn = sqlite3.connect(dbName)
  c = conn.cursor()

  # Create table
  c.execute('''CREATE TABLE extra (gene TEXT, genename TEXT, R2 DOUBLE,  `n.snps` INTEGER);''')
  c.execute('''CREATE TABLE weights (rsid TEXT, gene TEXT, weight DOUBLE, ref_allele CHARACTER, eff_allele CHARACTER, pval DOUBLE, N INTEGER, cis INTEGER);''')
  c.execute('''CREATE INDEX extra_gene ON extra (gene);''')
  c.execute('''CREATE INDEX weights_gene ON weights (gene);''')
  c.execute('''CREATE INDEX weights_rsid ON weights (rsid);''')
  c.execute('''CREATE INDEX weights_rsid_gene ON weights (rsid, gene);''')

  betaPath = "../Generate_ModelFits/Tenfold/BetaFiles/*enet.betas.txt"
  enetBetaFiles = [globName for globName in glob.glob(betaPath)]
  enetBetaGenes = [globName.split("/")[-1].split(".")[0] \
                   for globName in enetBetaFiles]

  for geneName, filePath in zip(enetBetaGenes, enetBetaFiles):
    with open(filePath,"r") as infh:
      numSnps = 0
      for line in infh:
        elements = line.strip().split()
        prefix = elements[0][:2]
        if prefix == "ch":
          snpid, beta = tuple(elements)
          snpinfo = snpid.split(".")
          # e.g. chr4.110692870.C.CAAAA
          ref, alt = snpinfo[-2], snpinfo[-1]
          c.execute("INSERT INTO weights VALUES ('%s','%s',%s,'%s','%s','','','')"%(snpid, geneName, beta, ref, alt))
          numSnps += 1
        elif prefix == "r2":
          if numSnps == 0:
            pass
          else:
            rsq = elements[1]
            c.execute("INSERT INTO extra VALUES ('%s','%s',%s,'%s')"%(geneName, geneName, rsq, numSnps))
            conn.commit()
        else:
          print line, geneName
          # raise Exception("Prefix should be 'ch' or 'rs'")

  conn.close()

if __name__ == "__main__":
  Main()
