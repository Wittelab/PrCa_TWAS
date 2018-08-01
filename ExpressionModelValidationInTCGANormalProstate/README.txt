# See below directory tree for structure and descriptions of directory items:

# Directory tree, generated via:
# `brew install tree`
# `tree`

.
├── 1MbpWindow_Predictions # Predictions of TCGA normal prostatic expression generated using `Prostate_Thibodeau.1MbpWindowSize.db` models
│   ├── chr1
│   │   └── predicted_expression.txt
│   ├── chr10
│   │   └── predicted_expression.txt
│   ├── chr11
│   │   └── predicted_expression.txt
│   ├── chr12
│   │   └── predicted_expression.txt
│   ├── chr13
│   │   └── predicted_expression.txt
│   ├── chr14
│   │   └── predicted_expression.txt
│   ├── chr15
│   │   └── predicted_expression.txt
│   ├── chr16
│   │   └── predicted_expression.txt
│   ├── chr17
│   │   └── predicted_expression.txt
│   ├── chr18
│   │   └── predicted_expression.txt
│   ├── chr19
│   │   └── predicted_expression.txt
│   ├── chr2
│   │   └── predicted_expression.txt
│   ├── chr20
│   │   └── predicted_expression.txt
│   ├── chr21
│   │   └── predicted_expression.txt
│   ├── chr22
│   │   └── predicted_expression.txt
│   ├── chr3
│   │   └── predicted_expression.txt
│   ├── chr4
│   │   └── predicted_expression.txt
│   ├── chr5
│   │   └── predicted_expression.txt
│   ├── chr6
│   │   └── predicted_expression.txt
│   ├── chr7
│   │   └── predicted_expression.txt
│   ├── chr8
│   │   └── predicted_expression.txt
│   └── chr9
│       └── predicted_expression.txt
├── ExpressionComparisons # Comparison of predicted/observed expression values for GTEx predictions vs. TCGA observed expression, 
│   │                     #                                                        our training models' predictions vs. TCGA observed expression,
│   │                     #                                                        and our training models' predictions vs. GTEx predictions
│   ├── Nonparametric     # Including comparisons measured via Spearman's correlation
│   │   ├── allchrs.gtex_vs_tcga.txt
│   │   ├── allchrs.mayo_vs_gtex.txt
│   │   ├── allchrs.mayo_vs_tcga.txt
│   │   ├── comparison.chr1.gtex_vs_tcga.txt
│   │   ├── comparison.chr1.mayo_vs_gtex.txt
│   │   ├── comparison.chr1.mayo_vs_tcga.txt
│   │   ├── comparison.chr10.gtex_vs_tcga.txt
│   │   ├── comparison.chr10.mayo_vs_gtex.txt
│   │   ├── comparison.chr10.mayo_vs_tcga.txt
│   │   ├── comparison.chr11.gtex_vs_tcga.txt
│   │   ├── comparison.chr11.mayo_vs_gtex.txt
│   │   ├── comparison.chr11.mayo_vs_tcga.txt
│   │   ├── comparison.chr12.gtex_vs_tcga.txt
│   │   ├── comparison.chr12.mayo_vs_gtex.txt
│   │   ├── comparison.chr12.mayo_vs_tcga.txt
│   │   ├── comparison.chr13.gtex_vs_tcga.txt
│   │   ├── comparison.chr13.mayo_vs_gtex.txt
│   │   ├── comparison.chr13.mayo_vs_tcga.txt
│   │   ├── comparison.chr14.gtex_vs_tcga.txt
│   │   ├── comparison.chr14.mayo_vs_gtex.txt
│   │   ├── comparison.chr14.mayo_vs_tcga.txt
│   │   ├── comparison.chr15.gtex_vs_tcga.txt
│   │   ├── comparison.chr15.mayo_vs_gtex.txt
│   │   ├── comparison.chr15.mayo_vs_tcga.txt
│   │   ├── comparison.chr16.gtex_vs_tcga.txt
│   │   ├── comparison.chr16.mayo_vs_gtex.txt
│   │   ├── comparison.chr16.mayo_vs_tcga.txt
│   │   ├── comparison.chr17.gtex_vs_tcga.txt
│   │   ├── comparison.chr17.mayo_vs_gtex.txt
│   │   ├── comparison.chr17.mayo_vs_tcga.txt
│   │   ├── comparison.chr18.gtex_vs_tcga.txt
│   │   ├── comparison.chr18.mayo_vs_gtex.txt
│   │   ├── comparison.chr18.mayo_vs_tcga.txt
│   │   ├── comparison.chr19.gtex_vs_tcga.txt
│   │   ├── comparison.chr19.mayo_vs_gtex.txt
│   │   ├── comparison.chr19.mayo_vs_tcga.txt
│   │   ├── comparison.chr2.gtex_vs_tcga.txt
│   │   ├── comparison.chr2.mayo_vs_gtex.txt
│   │   ├── comparison.chr2.mayo_vs_tcga.txt
│   │   ├── comparison.chr20.gtex_vs_tcga.txt
│   │   ├── comparison.chr20.mayo_vs_gtex.txt
│   │   ├── comparison.chr20.mayo_vs_tcga.txt
│   │   ├── comparison.chr21.gtex_vs_tcga.txt
│   │   ├── comparison.chr21.mayo_vs_gtex.txt
│   │   ├── comparison.chr21.mayo_vs_tcga.txt
│   │   ├── comparison.chr22.gtex_vs_tcga.txt
│   │   ├── comparison.chr22.mayo_vs_gtex.txt
│   │   ├── comparison.chr22.mayo_vs_tcga.txt
│   │   ├── comparison.chr3.gtex_vs_tcga.txt
│   │   ├── comparison.chr3.mayo_vs_gtex.txt
│   │   ├── comparison.chr3.mayo_vs_tcga.txt
│   │   ├── comparison.chr4.gtex_vs_tcga.txt
│   │   ├── comparison.chr4.mayo_vs_gtex.txt
│   │   ├── comparison.chr4.mayo_vs_tcga.txt
│   │   ├── comparison.chr5.gtex_vs_tcga.txt
│   │   ├── comparison.chr5.mayo_vs_gtex.txt
│   │   ├── comparison.chr5.mayo_vs_tcga.txt
│   │   ├── comparison.chr6.gtex_vs_tcga.txt
│   │   ├── comparison.chr6.mayo_vs_gtex.txt
│   │   ├── comparison.chr6.mayo_vs_tcga.txt
│   │   ├── comparison.chr7.gtex_vs_tcga.txt
│   │   ├── comparison.chr7.mayo_vs_gtex.txt
│   │   ├── comparison.chr7.mayo_vs_tcga.txt
│   │   ├── comparison.chr8.gtex_vs_tcga.txt
│   │   ├── comparison.chr8.mayo_vs_gtex.txt
│   │   ├── comparison.chr8.mayo_vs_tcga.txt
│   │   ├── comparison.chr9.gtex_vs_tcga.txt
│   │   ├── comparison.chr9.mayo_vs_gtex.txt
│   │   ├── comparison.chr9.mayo_vs_tcga.txt
│   │   └── logs
│   │       ├── chr1.log
│   │       ├── ...
│   ├── Parametric # Including comparisons measured via Pearson's correlation
│   │   ├── allchrs.gtex_vs_tcga.txt
│   │   ├── allchrs.mayo_vs_gtex.txt
│   │   ├── allchrs.mayo_vs_tcga.txt
│   │   ├── comparison.chr1.gtex_vs_tcga.txt
│   │   ├── comparison.chr1.mayo_vs_gtex.txt
│   │   ├── comparison.chr1.mayo_vs_tcga.txt
│   │   ├── comparison.chr10.gtex_vs_tcga.txt
│   │   ├── comparison.chr10.mayo_vs_gtex.txt
│   │   ├── comparison.chr10.mayo_vs_tcga.txt
│   │   ├── comparison.chr11.gtex_vs_tcga.txt
│   │   ├── comparison.chr11.mayo_vs_gtex.txt
│   │   ├── comparison.chr11.mayo_vs_tcga.txt
│   │   ├── comparison.chr12.gtex_vs_tcga.txt
│   │   ├── comparison.chr12.mayo_vs_gtex.txt
│   │   ├── comparison.chr12.mayo_vs_tcga.txt
│   │   ├── comparison.chr13.gtex_vs_tcga.txt
│   │   ├── comparison.chr13.mayo_vs_gtex.txt
│   │   ├── comparison.chr13.mayo_vs_tcga.txt
│   │   ├── comparison.chr14.gtex_vs_tcga.txt
│   │   ├── comparison.chr14.mayo_vs_gtex.txt
│   │   ├── comparison.chr14.mayo_vs_tcga.txt
│   │   ├── comparison.chr15.gtex_vs_tcga.txt
│   │   ├── comparison.chr15.mayo_vs_gtex.txt
│   │   ├── comparison.chr15.mayo_vs_tcga.txt
│   │   ├── comparison.chr16.gtex_vs_tcga.txt
│   │   ├── comparison.chr16.mayo_vs_gtex.txt
│   │   ├── comparison.chr16.mayo_vs_tcga.txt
│   │   ├── comparison.chr17.gtex_vs_tcga.txt
│   │   ├── comparison.chr17.mayo_vs_gtex.txt
│   │   ├── comparison.chr17.mayo_vs_tcga.txt
│   │   ├── comparison.chr18.gtex_vs_tcga.txt
│   │   ├── comparison.chr18.mayo_vs_gtex.txt
│   │   ├── comparison.chr18.mayo_vs_tcga.txt
│   │   ├── comparison.chr19.gtex_vs_tcga.txt
│   │   ├── comparison.chr19.mayo_vs_gtex.txt
│   │   ├── comparison.chr19.mayo_vs_tcga.txt
│   │   ├── comparison.chr2.gtex_vs_tcga.txt
│   │   ├── comparison.chr2.mayo_vs_gtex.txt
│   │   ├── comparison.chr2.mayo_vs_tcga.txt
│   │   ├── comparison.chr20.gtex_vs_tcga.txt
│   │   ├── comparison.chr20.mayo_vs_gtex.txt
│   │   ├── comparison.chr20.mayo_vs_tcga.txt
│   │   ├── comparison.chr21.gtex_vs_tcga.txt
│   │   ├── comparison.chr21.mayo_vs_gtex.txt
│   │   ├── comparison.chr21.mayo_vs_tcga.txt
│   │   ├── comparison.chr22.gtex_vs_tcga.txt
│   │   ├── comparison.chr22.mayo_vs_gtex.txt
│   │   ├── comparison.chr22.mayo_vs_tcga.txt
│   │   ├── comparison.chr3.gtex_vs_tcga.txt
│   │   ├── comparison.chr3.mayo_vs_gtex.txt
│   │   ├── comparison.chr3.mayo_vs_tcga.txt
│   │   ├── comparison.chr4.gtex_vs_tcga.txt
│   │   ├── comparison.chr4.mayo_vs_gtex.txt
│   │   ├── comparison.chr4.mayo_vs_tcga.txt
│   │   ├── comparison.chr5.gtex_vs_tcga.txt
│   │   ├── comparison.chr5.mayo_vs_gtex.txt
│   │   ├── comparison.chr5.mayo_vs_tcga.txt
│   │   ├── comparison.chr6.gtex_vs_tcga.txt
│   │   ├── comparison.chr6.mayo_vs_gtex.txt
│   │   ├── comparison.chr6.mayo_vs_tcga.txt
│   │   ├── comparison.chr7.gtex_vs_tcga.txt
│   │   ├── comparison.chr7.mayo_vs_gtex.txt
│   │   ├── comparison.chr7.mayo_vs_tcga.txt
│   │   ├── comparison.chr8.gtex_vs_tcga.txt
│   │   ├── comparison.chr8.mayo_vs_gtex.txt
│   │   ├── comparison.chr8.mayo_vs_tcga.txt
│   │   ├── comparison.chr9.gtex_vs_tcga.txt
│   │   ├── comparison.chr9.mayo_vs_gtex.txt
│   │   └── comparison.chr9.mayo_vs_tcga.txt
│   └── concatenate.sh
├── GTEx_Predictions # Predictions of TCGA normal prostatic expression generated using `TW_Prostate_0.5.db` GTEx v6p PredictDB models
│   ├── chr1
│   │   └── predicted_expression.txt
│   ├── chr10
│   │   └── predicted_expression.txt
│   ├── chr11
│   │   └── predicted_expression.txt
│   ├── chr12
│   │   └── predicted_expression.txt
│   ├── chr13
│   │   └── predicted_expression.txt
│   ├── chr14
│   │   └── predicted_expression.txt
│   ├── chr15
│   │   └── predicted_expression.txt
│   ├── chr16
│   │   └── predicted_expression.txt
│   ├── chr17
│   │   └── predicted_expression.txt
│   ├── chr18
│   │   └── predicted_expression.txt
│   ├── chr19
│   │   └── predicted_expression.txt
│   ├── chr2
│   │   └── predicted_expression.txt
│   ├── chr20
│   │   └── predicted_expression.txt
│   ├── chr21
│   │   └── predicted_expression.txt
│   ├── chr22
│   │   └── predicted_expression.txt
│   ├── chr3
│   │   └── predicted_expression.txt
│   ├── chr4
│   │   └── predicted_expression.txt
│   ├── chr5
│   │   └── predicted_expression.txt
│   ├── chr6
│   │   └── predicted_expression.txt
│   ├── chr7
│   │   └── predicted_expression.txt
│   ├── chr8
│   │   └── predicted_expression.txt
│   └── chr9
│       └── predicted_expression.txt
├── Generate_ModelFits # Files containing SNPs / Betas / r2 for expression prediction models (and used to generate `*.db` sqlite files below)
│   ├── 1MbpWindow     # LOOCV Models using dbGaP (Mayo Clinic) training data, with inclusion of imputed variants (r2 > 0.8) within 1Mb of gene boundaries
│   │   └── BetaFiles
│   │       ├── 1-2-SBSRNA4.enet.betas.txt
│   │       ├── ...
│   ├── LOOCV          # LOOCV Models using dbGaP (Mayo Clinic) training data, with inclusion of imputed variants (r2 > 0.8) within 500kb of gene boundaries
│   │   └── BetaFiles
│   │       ├── 1-2-SBSRNA4.enet.betas.txt
│   │       ├── ...
│   ├── Tenfold        # 10-fold CV Models using dbGaP (Mayo Clinic) training data, with inclusion of imputed variants (r2 > 0.8) within 500kb of gene boundaries
│   │   └── BetaFiles
│   │       ├── AADAT.enet.betas.txt
│   │       ├── ...
│   └── scripts        # Scripts for generating the `*.enet.betas.*` files above
│       ├── FitModels.AllMayoGenes.1MbpWindow.sh
│       ├── FitModels.AllMayoGenes.LOOCV.sh
│       ├── FitModels.GenesInBothGTExAndMayo.10FoldCV.sh
│       ├── FitModels.R
│       └── Genes_in_both_GTEx_and_Mayo.txt
├── Genotypes # Directory where individual-level (restricted/protected access) genotype files should be stored -- see `README.genotypes.txt`
│   └── README.genotypes.txt
├── Glmnet_Inputs # Directory where data and code for generating gene-centric genotype matrices for fitting expression models are located
│   ├── 1MbpWindow     # Data / scripts for generating precursors to LOOCV dbGaP (Mayo Clinic) training data models, with inclusion of imputed variants (r2 > 0.8) within 1Mb of gene boundaries
│   │   ├── README.glmnet_inputs.1MbpWindow.txt
│   │   ├── intermediates
│   │   └── scripts
│   │       ├── generate_gene_matrices.go
│   │       ├── header.txt
│   │       └── hg19_coords.bed
│   ├── README.glmnet_inputs.txt
│   ├── intermediates
│   └── scripts        # Data / scripts for generating precursors to LOOCV dbGaP (Mayo Clinic) training data models, with inclusion of imputed variants (r2 > 0.8) within 500kb of gene boundaries
│       ├── generate_gene_matrices.go
│       ├── header.txt
│       └── hg19_coords.bed
├── LOOCVand10FoldComparison # Comparison of predicted/observed expression values for our training models' predictions vs. TCGA observed expression,
│   │                        #                                                        analogous 10-fold CV models' predictions vs. TCGA observed expression,
│   │                        #                                                        and our training models' predictions vs. analogous 10-fold CV models' predictions
│   ├── Nonparametric        # Including comparisons measured via Spearman's correlation
│   │   ├── allchrs.loocv_vs_tcga.txt
│   │   ├── allchrs.tenfold_vs_loocv.txt
│   │   ├── allchrs.tenfold_vs_tcga.txt
│   │   ├── comparison.chr1.loocv_vs_tcga.txt
│   │   ├── comparison.chr1.tenfold_vs_loocv.txt
│   │   ├── comparison.chr1.tenfold_vs_tcga.txt
│   │   ├── comparison.chr10.loocv_vs_tcga.txt
│   │   ├── comparison.chr10.tenfold_vs_loocv.txt
│   │   ├── comparison.chr10.tenfold_vs_tcga.txt
│   │   ├── comparison.chr11.loocv_vs_tcga.txt
│   │   ├── comparison.chr11.tenfold_vs_loocv.txt
│   │   ├── comparison.chr11.tenfold_vs_tcga.txt
│   │   ├── comparison.chr12.loocv_vs_tcga.txt
│   │   ├── comparison.chr12.tenfold_vs_loocv.txt
│   │   ├── comparison.chr12.tenfold_vs_tcga.txt
│   │   ├── comparison.chr13.loocv_vs_tcga.txt
│   │   ├── comparison.chr13.tenfold_vs_loocv.txt
│   │   ├── comparison.chr13.tenfold_vs_tcga.txt
│   │   ├── comparison.chr14.loocv_vs_tcga.txt
│   │   ├── comparison.chr14.tenfold_vs_loocv.txt
│   │   ├── comparison.chr14.tenfold_vs_tcga.txt
│   │   ├── comparison.chr15.loocv_vs_tcga.txt
│   │   ├── comparison.chr15.tenfold_vs_loocv.txt
│   │   ├── comparison.chr15.tenfold_vs_tcga.txt
│   │   ├── comparison.chr16.loocv_vs_tcga.txt
│   │   ├── comparison.chr16.tenfold_vs_loocv.txt
│   │   ├── comparison.chr16.tenfold_vs_tcga.txt
│   │   ├── comparison.chr17.loocv_vs_tcga.txt
│   │   ├── comparison.chr17.tenfold_vs_loocv.txt
│   │   ├── comparison.chr17.tenfold_vs_tcga.txt
│   │   ├── comparison.chr18.loocv_vs_tcga.txt
│   │   ├── comparison.chr18.tenfold_vs_loocv.txt
│   │   ├── comparison.chr18.tenfold_vs_tcga.txt
│   │   ├── comparison.chr19.loocv_vs_tcga.txt
│   │   ├── comparison.chr19.tenfold_vs_loocv.txt
│   │   ├── comparison.chr19.tenfold_vs_tcga.txt
│   │   ├── comparison.chr2.loocv_vs_tcga.txt
│   │   ├── comparison.chr2.tenfold_vs_loocv.txt
│   │   ├── comparison.chr2.tenfold_vs_tcga.txt
│   │   ├── comparison.chr20.loocv_vs_tcga.txt
│   │   ├── comparison.chr20.tenfold_vs_loocv.txt
│   │   ├── comparison.chr20.tenfold_vs_tcga.txt
│   │   ├── comparison.chr21.loocv_vs_tcga.txt
│   │   ├── comparison.chr21.tenfold_vs_loocv.txt
│   │   ├── comparison.chr21.tenfold_vs_tcga.txt
│   │   ├── comparison.chr22.loocv_vs_tcga.txt
│   │   ├── comparison.chr22.tenfold_vs_loocv.txt
│   │   ├── comparison.chr22.tenfold_vs_tcga.txt
│   │   ├── comparison.chr3.loocv_vs_tcga.txt
│   │   ├── comparison.chr3.tenfold_vs_loocv.txt
│   │   ├── comparison.chr3.tenfold_vs_tcga.txt
│   │   ├── comparison.chr4.loocv_vs_tcga.txt
│   │   ├── comparison.chr4.tenfold_vs_loocv.txt
│   │   ├── comparison.chr4.tenfold_vs_tcga.txt
│   │   ├── comparison.chr5.loocv_vs_tcga.txt
│   │   ├── comparison.chr5.tenfold_vs_loocv.txt
│   │   ├── comparison.chr5.tenfold_vs_tcga.txt
│   │   ├── comparison.chr6.loocv_vs_tcga.txt
│   │   ├── comparison.chr6.tenfold_vs_loocv.txt
│   │   ├── comparison.chr6.tenfold_vs_tcga.txt
│   │   ├── comparison.chr7.loocv_vs_tcga.txt
│   │   ├── comparison.chr7.tenfold_vs_loocv.txt
│   │   ├── comparison.chr7.tenfold_vs_tcga.txt
│   │   ├── comparison.chr8.loocv_vs_tcga.txt
│   │   ├── comparison.chr8.tenfold_vs_loocv.txt
│   │   ├── comparison.chr8.tenfold_vs_tcga.txt
│   │   ├── comparison.chr9.loocv_vs_tcga.txt
│   │   ├── comparison.chr9.tenfold_vs_loocv.txt
│   │   ├── comparison.chr9.tenfold_vs_tcga.txt
│   │   └── logs
│   │       ├── chr1.log
│   │       ├── ...
│   ├── Parametric        # Including comparisons measured via Pearson's correlation
│   │   ├── allchrs.loocv_vs_tcga.txt
│   │   ├── allchrs.tenfold_vs_loocv.txt
│   │   ├── allchrs.tenfold_vs_tcga.txt
│   │   ├── comparison.chr1.loocv_vs_tcga.txt
│   │   ├── comparison.chr1.tenfold_vs_loocv.txt
│   │   ├── comparison.chr1.tenfold_vs_tcga.txt
│   │   ├── comparison.chr10.loocv_vs_tcga.txt
│   │   ├── comparison.chr10.tenfold_vs_loocv.txt
│   │   ├── comparison.chr10.tenfold_vs_tcga.txt
│   │   ├── comparison.chr11.loocv_vs_tcga.txt
│   │   ├── comparison.chr11.tenfold_vs_loocv.txt
│   │   ├── comparison.chr11.tenfold_vs_tcga.txt
│   │   ├── comparison.chr12.loocv_vs_tcga.txt
│   │   ├── comparison.chr12.tenfold_vs_loocv.txt
│   │   ├── comparison.chr12.tenfold_vs_tcga.txt
│   │   ├── comparison.chr13.loocv_vs_tcga.txt
│   │   ├── comparison.chr13.tenfold_vs_loocv.txt
│   │   ├── comparison.chr13.tenfold_vs_tcga.txt
│   │   ├── comparison.chr14.loocv_vs_tcga.txt
│   │   ├── comparison.chr14.tenfold_vs_loocv.txt
│   │   ├── comparison.chr14.tenfold_vs_tcga.txt
│   │   ├── comparison.chr15.loocv_vs_tcga.txt
│   │   ├── comparison.chr15.tenfold_vs_loocv.txt
│   │   ├── comparison.chr15.tenfold_vs_tcga.txt
│   │   ├── comparison.chr16.loocv_vs_tcga.txt
│   │   ├── comparison.chr16.tenfold_vs_loocv.txt
│   │   ├── comparison.chr16.tenfold_vs_tcga.txt
│   │   ├── comparison.chr17.loocv_vs_tcga.txt
│   │   ├── comparison.chr17.tenfold_vs_loocv.txt
│   │   ├── comparison.chr17.tenfold_vs_tcga.txt
│   │   ├── comparison.chr18.loocv_vs_tcga.txt
│   │   ├── comparison.chr18.tenfold_vs_loocv.txt
│   │   ├── comparison.chr18.tenfold_vs_tcga.txt
│   │   ├── comparison.chr19.loocv_vs_tcga.txt
│   │   ├── comparison.chr19.tenfold_vs_loocv.txt
│   │   ├── comparison.chr19.tenfold_vs_tcga.txt
│   │   ├── comparison.chr2.loocv_vs_tcga.txt
│   │   ├── comparison.chr2.tenfold_vs_loocv.txt
│   │   ├── comparison.chr2.tenfold_vs_tcga.txt
│   │   ├── comparison.chr20.loocv_vs_tcga.txt
│   │   ├── comparison.chr20.tenfold_vs_loocv.txt
│   │   ├── comparison.chr20.tenfold_vs_tcga.txt
│   │   ├── comparison.chr21.loocv_vs_tcga.txt
│   │   ├── comparison.chr21.tenfold_vs_loocv.txt
│   │   ├── comparison.chr21.tenfold_vs_tcga.txt
│   │   ├── comparison.chr22.loocv_vs_tcga.txt
│   │   ├── comparison.chr22.tenfold_vs_loocv.txt
│   │   ├── comparison.chr22.tenfold_vs_tcga.txt
│   │   ├── comparison.chr3.loocv_vs_tcga.txt
│   │   ├── comparison.chr3.tenfold_vs_loocv.txt
│   │   ├── comparison.chr3.tenfold_vs_tcga.txt
│   │   ├── comparison.chr4.loocv_vs_tcga.txt
│   │   ├── comparison.chr4.tenfold_vs_loocv.txt
│   │   ├── comparison.chr4.tenfold_vs_tcga.txt
│   │   ├── comparison.chr5.loocv_vs_tcga.txt
│   │   ├── comparison.chr5.tenfold_vs_loocv.txt
│   │   ├── comparison.chr5.tenfold_vs_tcga.txt
│   │   ├── comparison.chr6.loocv_vs_tcga.txt
│   │   ├── comparison.chr6.tenfold_vs_loocv.txt
│   │   ├── comparison.chr6.tenfold_vs_tcga.txt
│   │   ├── comparison.chr7.loocv_vs_tcga.txt
│   │   ├── comparison.chr7.tenfold_vs_loocv.txt
│   │   ├── comparison.chr7.tenfold_vs_tcga.txt
│   │   ├── comparison.chr8.loocv_vs_tcga.txt
│   │   ├── comparison.chr8.tenfold_vs_loocv.txt
│   │   ├── comparison.chr8.tenfold_vs_tcga.txt
│   │   ├── comparison.chr9.loocv_vs_tcga.txt
│   │   ├── comparison.chr9.tenfold_vs_loocv.txt
│   │   └── comparison.chr9.tenfold_vs_tcga.txt
│   └── concatenate.sh
├── Mayo_Predictions # Predictions of TCGA normal prostatic expression generated using our `Prostate_Thibodeau.db` dbGaP (Mayo Clinic) training data models
│   ├── MayoVsTCGAComparison # Comparison of predicted/observed expression values for our training models' predictions vs. TCGA observed expression
│   │   ├── Nonparametric    # Including comparisons measured via Spearman's correlation
│   │   │   ├── allchrs.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr1.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr10.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr11.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr12.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr13.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr14.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr15.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr16.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr17.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr18.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr19.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr2.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr20.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr21.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr22.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr3.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr4.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr5.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr6.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr7.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr8.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr9.all_mayo_vs_tcga.txt
│   │   │   └── logs
│   │   │       ├── chr1.log
│   │   │       ├── ...
│   │   ├── Parametric        # Including comparisons measured via Pearson's correlation
│   │   │   ├── allchrs.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr1.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr10.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr11.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr12.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr13.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr14.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr15.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr16.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr17.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr18.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr19.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr2.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr20.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr21.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr22.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr3.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr4.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr5.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr6.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr7.all_mayo_vs_tcga.txt
│   │   │   ├── comparison.chr8.all_mayo_vs_tcga.txt
│   │   │   └── comparison.chr9.all_mayo_vs_tcga.txt
│   │   └── concatenate.sh
│   ├── chr1
│   │   └── predicted_expression.txt
│   ├── chr10
│   │   └── predicted_expression.txt
│   ├── chr11
│   │   └── predicted_expression.txt
│   ├── chr12
│   │   └── predicted_expression.txt
│   ├── chr13
│   │   └── predicted_expression.txt
│   ├── chr14
│   │   └── predicted_expression.txt
│   ├── chr15
│   │   └── predicted_expression.txt
│   ├── chr16
│   │   └── predicted_expression.txt
│   ├── chr17
│   │   └── predicted_expression.txt
│   ├── chr18
│   │   └── predicted_expression.txt
│   ├── chr19
│   │   └── predicted_expression.txt
│   ├── chr2
│   │   └── predicted_expression.txt
│   ├── chr20
│   │   └── predicted_expression.txt
│   ├── chr21
│   │   └── predicted_expression.txt
│   ├── chr22
│   │   └── predicted_expression.txt
│   ├── chr3
│   │   └── predicted_expression.txt
│   ├── chr4
│   │   └── predicted_expression.txt
│   ├── chr5
│   │   └── predicted_expression.txt
│   ├── chr6
│   │   └── predicted_expression.txt
│   ├── chr7
│   │   └── predicted_expression.txt
│   ├── chr8
│   │   └── predicted_expression.txt
│   └── chr9
│       └── predicted_expression.txt
├── README.directory.txt
├── Sample_Files # Files with sample ID's
│   ├── All_TCGA_SampleIDs.txt
│   ├── Getting_TCGA_IDs.txt
│   ├── TCGA_Sample_IDs.txt
│   ├── TCGA_Samples_With_Genotypes.samples
│   └── TCGA_Samples_With_Genotypes.txt
├── TCGA_ObservedNormalExpression # Matrix of normal expression data downloaded / concatenated from NCBI GDC and converted from gene ensembl ID's to HGNC common names
│   └── TCGA_Normal_Expression_Matrix.HGNC.txt
├── TenfoldCV_Predictions         # Predictions of TCGA normal prostatic expression generated using our 10-fold cross-validated `Prostate_Thibodeau.10foldCV.db` models
│   ├── chr1
│   │   └── predicted_expression.txt
│   ├── chr10
│   │   └── predicted_expression.txt
│   ├── chr11
│   │   └── predicted_expression.txt
│   ├── chr12
│   │   └── predicted_expression.txt
│   ├── chr13
│   │   └── predicted_expression.txt
│   ├── chr14
│   │   └── predicted_expression.txt
│   ├── chr15
│   │   └── predicted_expression.txt
│   ├── chr16
│   │   └── predicted_expression.txt
│   ├── chr17
│   │   └── predicted_expression.txt
│   ├── chr18
│   │   └── predicted_expression.txt
│   ├── chr19
│   │   └── predicted_expression.txt
│   ├── chr2
│   │   └── predicted_expression.txt
│   ├── chr20
│   │   └── predicted_expression.txt
│   ├── chr21
│   │   └── predicted_expression.txt
│   ├── chr22
│   │   └── predicted_expression.txt
│   ├── chr3
│   │   └── predicted_expression.txt
│   ├── chr4
│   │   └── predicted_expression.txt
│   ├── chr5
│   │   └── predicted_expression.txt
│   ├── chr6
│   │   └── predicted_expression.txt
│   ├── chr7
│   │   └── predicted_expression.txt
│   ├── chr8
│   │   └── predicted_expression.txt
│   ├── chr9
│   │   └── predicted_expression.txt
│   └── logs
│       ├── chr1.log
│       ├── ...
├── WindowSizeComparison  # Comparison of predicted/observed expression values for our training models' predictions vs. TCGA observed expression,
│   │                     #                                                        predictions from analogous models of all variants within 1Mb vs. TCGA observed expression,
│   │                     #                                                        and our training models' predictions vs. predictions from analogous models of all variants within 1Mb
│   ├── Nonparametric     # Including comparisons measured via Spearman's correlation
│   │   ├── allchrs.fivehundredkbp_vs_onembp.txt
│   │   ├── allchrs.fivehundredkbp_vs_tcga.txt
│   │   ├── allchrs.onembp_vs_tcga.txt
│   │   ├── comparison.chr1.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr1.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr1.log
│   │   ├── comparison.chr1.onembp_vs_tcga.txt
│   │   ├── comparison.chr10.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr10.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr10.log
│   │   ├── comparison.chr10.onembp_vs_tcga.txt
│   │   ├── comparison.chr11.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr11.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr11.log
│   │   ├── comparison.chr11.onembp_vs_tcga.txt
│   │   ├── comparison.chr12.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr12.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr12.log
│   │   ├── comparison.chr12.onembp_vs_tcga.txt
│   │   ├── comparison.chr13.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr13.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr13.log
│   │   ├── comparison.chr13.onembp_vs_tcga.txt
│   │   ├── comparison.chr14.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr14.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr14.log
│   │   ├── comparison.chr14.onembp_vs_tcga.txt
│   │   ├── comparison.chr15.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr15.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr15.log
│   │   ├── comparison.chr15.onembp_vs_tcga.txt
│   │   ├── comparison.chr16.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr16.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr16.log
│   │   ├── comparison.chr16.onembp_vs_tcga.txt
│   │   ├── comparison.chr17.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr17.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr17.log
│   │   ├── comparison.chr17.onembp_vs_tcga.txt
│   │   ├── comparison.chr18.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr18.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr18.log
│   │   ├── comparison.chr18.onembp_vs_tcga.txt
│   │   ├── comparison.chr19.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr19.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr19.log
│   │   ├── comparison.chr19.onembp_vs_tcga.txt
│   │   ├── comparison.chr2.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr2.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr2.log
│   │   ├── comparison.chr2.onembp_vs_tcga.txt
│   │   ├── comparison.chr20.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr20.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr20.log
│   │   ├── comparison.chr20.onembp_vs_tcga.txt
│   │   ├── comparison.chr21.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr21.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr21.log
│   │   ├── comparison.chr21.onembp_vs_tcga.txt
│   │   ├── comparison.chr22.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr22.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr22.log
│   │   ├── comparison.chr22.onembp_vs_tcga.txt
│   │   ├── comparison.chr3.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr3.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr3.log
│   │   ├── comparison.chr3.onembp_vs_tcga.txt
│   │   ├── comparison.chr4.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr4.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr4.log
│   │   ├── comparison.chr4.onembp_vs_tcga.txt
│   │   ├── comparison.chr5.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr5.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr5.log
│   │   ├── comparison.chr5.onembp_vs_tcga.txt
│   │   ├── comparison.chr6.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr6.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr6.log
│   │   ├── comparison.chr6.onembp_vs_tcga.txt
│   │   ├── comparison.chr7.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr7.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr7.log
│   │   ├── comparison.chr7.onembp_vs_tcga.txt
│   │   ├── comparison.chr8.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr8.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr8.log
│   │   ├── comparison.chr8.onembp_vs_tcga.txt
│   │   ├── comparison.chr9.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr9.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr9.log
│   │   ├── comparison.chr9.onembp_vs_tcga.txt
│   │   └── test_correlation.R
│   ├── Parametric        # Including comparisons measured via Spearman's correlation
│   │   ├── allchrs.fivehundredkbp_vs_onembp.txt
│   │   ├── allchrs.fivehundredkbp_vs_tcga.txt
│   │   ├── allchrs.onembp_vs_tcga.txt
│   │   ├── comparison.chr1.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr1.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr1.log
│   │   ├── comparison.chr1.onembp_vs_tcga.txt
│   │   ├── comparison.chr10.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr10.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr10.log
│   │   ├── comparison.chr10.onembp_vs_tcga.txt
│   │   ├── comparison.chr11.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr11.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr11.log
│   │   ├── comparison.chr11.onembp_vs_tcga.txt
│   │   ├── comparison.chr12.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr12.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr12.log
│   │   ├── comparison.chr12.onembp_vs_tcga.txt
│   │   ├── comparison.chr13.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr13.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr13.log
│   │   ├── comparison.chr13.onembp_vs_tcga.txt
│   │   ├── comparison.chr14.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr14.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr14.log
│   │   ├── comparison.chr14.onembp_vs_tcga.txt
│   │   ├── comparison.chr15.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr15.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr15.log
│   │   ├── comparison.chr15.onembp_vs_tcga.txt
│   │   ├── comparison.chr16.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr16.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr16.log
│   │   ├── comparison.chr16.onembp_vs_tcga.txt
│   │   ├── comparison.chr17.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr17.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr17.log
│   │   ├── comparison.chr17.onembp_vs_tcga.txt
│   │   ├── comparison.chr18.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr18.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr18.log
│   │   ├── comparison.chr18.onembp_vs_tcga.txt
│   │   ├── comparison.chr19.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr19.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr19.log
│   │   ├── comparison.chr19.onembp_vs_tcga.txt
│   │   ├── comparison.chr2.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr2.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr2.log
│   │   ├── comparison.chr2.onembp_vs_tcga.txt
│   │   ├── comparison.chr20.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr20.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr20.log
│   │   ├── comparison.chr20.onembp_vs_tcga.txt
│   │   ├── comparison.chr21.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr21.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr21.log
│   │   ├── comparison.chr21.onembp_vs_tcga.txt
│   │   ├── comparison.chr22.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr22.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr22.log
│   │   ├── comparison.chr22.onembp_vs_tcga.txt
│   │   ├── comparison.chr3.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr3.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr3.log
│   │   ├── comparison.chr3.onembp_vs_tcga.txt
│   │   ├── comparison.chr4.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr4.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr4.log
│   │   ├── comparison.chr4.onembp_vs_tcga.txt
│   │   ├── comparison.chr5.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr5.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr5.log
│   │   ├── comparison.chr5.onembp_vs_tcga.txt
│   │   ├── comparison.chr6.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr6.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr6.log
│   │   ├── comparison.chr6.onembp_vs_tcga.txt
│   │   ├── comparison.chr7.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr7.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr7.log
│   │   ├── comparison.chr7.onembp_vs_tcga.txt
│   │   ├── comparison.chr8.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr8.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr8.log
│   │   ├── comparison.chr8.onembp_vs_tcga.txt
│   │   ├── comparison.chr9.fivehundredkbp_vs_onembp.txt
│   │   ├── comparison.chr9.fivehundredkbp_vs_tcga.txt
│   │   ├── comparison.chr9.log
│   │   ├── comparison.chr9.onembp_vs_tcga.txt
│   │   └── test_correlation.R
│   └── concatenate.sh
├── dbSNP # vcf of dbSNP rsids
│   ├── All_20180423.vcf.gz
│   ├── All_20180423.vcf.gz.tbi
│   └── annotation.sh
├── dbs   # SQLite Databases containing expression prediction models
│   ├── Prostate_Thibodeau.10foldCV.db
│   ├── Prostate_Thibodeau.1MbpWindowSize.db
│   ├── Prostate_Thibodeau.db
│   ├── TW_Prostate_0.5.db
│   └── prostate_chrdb.pkl
├── headers
│   ├── chr1.dose.reheader.txt
│   ├── chr10.dose.reheader.txt
│   ├── chr11.dose.reheader.txt
│   ├── chr12.dose.reheader.txt
│   ├── chr13.dose.reheader.txt
│   ├── chr14.dose.reheader.txt
│   ├── chr15.dose.reheader.txt
│   ├── chr16.dose.reheader.txt
│   ├── chr17.dose.reheader.txt
│   ├── chr18.dose.reheader.txt
│   ├── chr19.dose.reheader.txt
│   ├── chr2.dose.reheader.txt
│   ├── chr20.dose.reheader.txt
│   ├── chr21.dose.reheader.txt
│   ├── chr22.dose.reheader.txt
│   ├── chr3.dose.reheader.txt
│   ├── chr4.dose.reheader.txt
│   ├── chr5.dose.reheader.txt
│   ├── chr6.dose.reheader.txt
│   ├── chr7.dose.reheader.txt
│   ├── chr8.dose.reheader.txt
│   └── chr9.dose.reheader.txt
└── scripts # Scripts for running imputation predictions / comparisons / database generation
    ├── Compare1MBand500KB.R
    ├── Compare1MBand500KB.nonparametric.R
    ├── Compare1MBand500KB.nonparametric.sh
    ├── Compare1MBand500KB.sh
    ├── CompareLOOCVand10Fold.R
    ├── CompareLOOCVand10Fold.nonparametric.R
    ├── CompareLOOCVand10Fold.nonparametric.sh
    ├── CompareLOOCVand10Fold.sh
    ├── CompareMayoGTExTCGA.R
    ├── CompareMayoGTExTCGA.nonparametric.R
    ├── CompareMayoGTExTCGA.nonparametric.sh
    ├── CompareMayoGTExTCGA.sh
    ├── CompareMayoTCGA.R
    ├── CompareMayoTCGA.nonparametric.R
    ├── CompareMayoTCGA.nonparametric.sh
    ├── CompareMayoTCGA.sh
    ├── PrediXcan.CHR.multipleInputs.gen_rsid.TW_Prostate_0.5.py
    ├── PrediXcan.VCF.py
    ├── make_10foldCV_db.py
    ├── make_windowsize_db.py
    ├── tcga_imputation.sh
    ├── tcga_preprocess.sh
    └── usage.sh
