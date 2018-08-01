#!/usr/bin/env python

import os, sys

def revComp(allele):
  revDict = {"A":"T","C":"G","G":"C","T":"A","-":"-"}
  return "".join([revDict[allele[i].upper()] for i in range(len(allele)-1,-1,-1)])

# CHROM   POS     ID          REF     ALT     AC      AN      AF         AC_EXCLUDING_1000G  AN_EXCLUDING_1000G  AF_EXCLUDING_1000G  AA
# 17      13043   rs17054921  C       A       792     64940   0.0121959  642                 59950               0.0107089           C
# 17      50911   rs11658619  A       G       39703   64940   0.61138    36559               59950               0.609825            A
def parse_mafs():
  maf_dicts = []
  for chromosome in range(1,23):
    maf_dict = {}
    with open("chr%s.tabix_out.txt" % (str(chromosome),),"r") as infh:
      for line in infh:
        elements = line.strip().split()
        chrom, pos, id, ref, alt, ac, an, af, afex1g, anex1g, afex1g, aa = tuple(elements)
        if ":".join([chrom, pos]) not in maf_dict:
          maf_dict[":".join([chrom, pos])] = [(ref, alt, float(af), float(afex1g)),]
        else:
          maf_dict[":".join([chrom, pos])].append((ref, alt, float(af), float(afex1g)))
    maf_dicts.append(maf_dict)
  return maf_dicts

def main():
  maf_dicts = parse_mafs()
  all_modeled_mafs = {}

  # chr18.bed.txt
  # 18      22109   22109   chr18.22109.T.G
  # 18      48740   48740   chr18.48740.A.C
  # 18      63101   63101   chr18.63101.C.T
  for chromosome in range(1,23):
    print "Matching chr%s SNPs..." % (str(chromosome),)
    with open("chr%s.bed.txt" % (str(chromosome),),"r") as infh:
      for line in infh:
        elements = line.strip().split()
        chr, pos, pos_end, snpid = tuple(elements)
        bp_key = ":".join([chr, pos])
        alleles = snpid.split(".")[2:]
        ref, alt = alleles[0], alleles[1]
        snp_match_info = match_snp((snpid, bp_key, ref, alt), maf_dicts[chromosome-1])
        is_match, match_af = tuple(snp_match_info)
        if is_match:
          match_maf = 1.0 - match_af if match_af > 0.5 else match_af
          all_modeled_mafs[snpid] = match_maf

  print "\nNumber of Modeled Autosomal Variants with HRC MAF:", len(all_modeled_mafs.keys())
  sorted_mafs = sorted(all_modeled_mafs.values())
  print "Percent of Variants >= 1% MAF:", float(len([maf for maf in sorted_mafs if maf >= 0.01])) / float(len(sorted_mafs))
  print "Percent of Variants >= 5% MAF:", float(len([maf for maf in sorted_mafs if maf >= 0.05])) / float(len(sorted_mafs))

def match_snp(query_tuple, maf_dict):
  query_id, query_bp, query_ref, query_alt = query_tuple
  if query_bp not in maf_dict:
    print "%s MAF not in HRC -- continuing" % (query_id)
    return (0, 0.0)
  else:
    values = maf_dict[query_bp]
    if len(values) < 2:
      hrc_ref, hrc_alt, hrc_af, hrc_afex1g = tuple(values[0])
      if allele_match(query_ref, query_alt, hrc_ref, hrc_alt):
        return (1, hrc_af)
      else:
        return (0, 0.0)
    else:
      for value in values:
        hrc_ref, hrc_alt, hrc_af, hrc_afex1g = tuple(value)
        if allele_match(query_ref, query_alt, hrc_ref, hrc_alt):
          return (1, hrc_af)
        else:
          return (0, 0.0)
      return (0, 0.0)
      
def allele_match(query_ref, query_alt, hrc_ref, hrc_alt):
  if query_ref == hrc_ref and query_alt == hrc_alt:
    return 1
  elif query_ref == revComp(hrc_ref) and query_alt == revComp(hrc_alt):
    return 1
  elif query_ref == hrc_alt and query_alt == hrc_ref:
    return 1
  elif query_ref == revComp(hrc_alt) and query_alt == revComp(hrc_ref):
    return 1
  else:
    return 0

if __name__ == "__main__":
  main()
