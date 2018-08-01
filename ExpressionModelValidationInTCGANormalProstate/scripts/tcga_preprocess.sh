cd ..

# wget ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/All_20180423.vcf.gz
# mv All_20180423.vcf.gz ../dbSNP
# tabix ../dbSNP/All_20180423.vcf.gz

for CHR in {1..22}
do bcftools reheader --header ../headers/chr${CHR}.dose.reheader.txt \
                     ../Genotypes/chr${CHR}_rsq05.dose.vcf.gz | \
   bcftools view --samples-file ../Sample_Files/TCGA_Sample_IDs.txt \
                 --force-samples -O z -o ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz

   tabix ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz

   mkdir /scratch/emamin
   mkdir /scratch/emamin/TWAS/
   mkdir /scratch/emamin/TWAS/chr${CHR}/

   bcftools annotate \
            --annotations ../dbSNP/All_20180423.vcf.gz \
            --columns ID \
            --output ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.rsid_annotated.vcf.gz \
            --output-type z \
            ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz
done
