Predicted TCGA Normal Prostatic Expression used for our discovery/association analyses
                                            Imputed using `Prostate_Thibodeau.db`
                                            and germline TCGA genotypes (r2_info > 0.5)

`MayoVsTCGAComparison` --> Correlation(s) between predicted expression described above
                           and true, observed RNA-Seq expression measured in TCGA normal
                           prostate tissue (and downloaded from NCBI Genomic Data Commons,
                           where it's available with unrestricted access)
  Parametric --> using linear regression (equivalent to Pearson's correlation)
  Nonparametric --> also uses Spearman's rank correlation, making no distributional assumptions
