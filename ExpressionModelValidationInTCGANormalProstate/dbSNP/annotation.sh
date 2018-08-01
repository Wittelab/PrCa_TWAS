cd /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/dbSNP
# wget ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/All_20180423.vcf.gz

tabix /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/chr21.tcga_normal_tissue.dose.vcf.gz
tabix /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/dbSNP/All_20180423.vcf.gz

bcftools annotate --annotations /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/dbSNP/All_20180423.vcf.gz \
                  --columns ID \
                  --output /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/dbSNP/chr21.tcga_normal_tissue.dose.rsid_annotated.vcf.gz \
                  --output-type z \
                  /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/chr21.tcga_normal_tissue.dose.vcf.gz
