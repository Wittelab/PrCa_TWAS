# For Linux -- alternatively, have Python2.7 with NumPy in $PATH
# module load python/2.7.10
# module load numpy/1.10.1/python.2.7.10 

python2.7 PrediXcan.VCF.py --predict --chromosome 21 \
                           --dosages /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/ \
                           --dosages_prefix chr21.tcga_normal_tissue \
                           --weights /wittelab/data1/emamin/TWAS/dbs/Prostate_Thibodeau.db \
                           --output_dir /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/Mayo_Predictions/chr21/ \
                           --samples /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/TCGA_Samples_With_Genotypes.samples

python2.7 PrediXcan.VCF.py --predict --chromosome 21 \
                           --dosages /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/dbSNP/ \
                           --dosages_prefix chr21.tcga_normal_tissue.dose.rsid_annotated \
                           --weights /wittelab/data1/emamin/TWAS/dbs/GTEx-V6p-HapMap-2016-09-08/TW_Prostate_0.5.db \
                           --output_dir /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/GTEx_Predictions/chr21/ \
                           --samples /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/TCGA_Samples_With_Genotypes.samples \
                           --use_rsid
