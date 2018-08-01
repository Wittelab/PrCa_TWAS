Note: Inputs for GLMNet model fitting (i.e. with script "../Generate_ModelFits/scripts/FitModels.AllMayoGenes.LOOCV.sh")
      can be generated with the scripts included here, contingent on access to the restricted dbGaP phs000985 repository.
      As described in our manscript methods, we phased (Eagle v2.3.5) and imputed (Beagle v4.1) these data, and filtered
      variants with r2 info less than 0.8. These steps produced the files "../Genotypes/chr${CHR}.dbGaP.r2gt0.8.vcf.gz",
      where ${CHR} ranges from 1 to 22, expected as an input to the scripts provided in this repository.

Dependencies: golang v1.8+
              GNU awk
