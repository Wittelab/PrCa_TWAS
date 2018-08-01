Note: The TCGA Normal Tissue Genotypes are available with restricted access to authorized researchers.
      With approval, these files can be downloaded from the NIH/NCI Genomic Data Commons (gdc.cancer.gov).
      As described in our manuscript methods, we phased and imputed these files using the UMich Imputation
      Server (imputationserver.sph.umich.edu), and filtered variants with r2 info less than 0.5. These
      steps produced the files "chr${CHR}_rsq05.dose.vcf.gz", where ${CHR} ranges from 1 to 22, expected
      as an input to the scripts provided in this repository.
