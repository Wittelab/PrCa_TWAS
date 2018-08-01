# Downloaded already
# wget ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/All_20180423.vcf.gz
# mv All_20180423.vcf.gz ../dbSNP
# tabix ../dbSNP/All_20180423.vcf.gz
# tabix ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz

for CHR in {1..22};
do bcftools reheader --header ../headers/chr${CHR}.dose.reheader.txt \
                     ../Genotypes/TCGA/chr${CHR}_rsq05.dose.vcf.gz | \
   bcftools view --samples-file ../Sample_Files/TCGA_Sample_IDs.txt \
                 --force-samples -O z -o ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz

   # For Linux -- alternatively, have Python2.7 with NumPy in $PATH
   # module load python/2.7.10
   # module load numpy/1.10.1/python.2.7.10 

   python2.7 scripts/PrediXcan.VCF.py --predict --chromosome ${CHR} \
                              --dosages ../Genotypes/ \
                              --dosages_prefix chr${CHR}.tcga_normal_tissue \
                              --weights ../dbs/Prostate_Thibodeau.db \
                              --output_dir ../Mayo_Predictions/chr${CHR}/ \
                              --samples ../Sample_Files/TCGA_Samples_With_Genotypes.samples

   python2.7 scripts/PrediXcan.VCF.py --predict --chromosome ${CHR} \
                              --dosages ../Genotypes/ \
                              --dosages_prefix chr${CHR}.tcga_normal_tissue \
                              --weights ../dbs/Prostate_Thibodeau.10foldCV.db \
                              --output_dir ../TenfoldCV_Predictions/chr${CHR}/ \
                              --samples ../Sample_Files/TCGA_Samples_With_Genotypes.samples

   python2.7 scripts/PrediXcan.VCF.py --predict --chromosome ${CHR} \
                              --dosages ../Genotypes/ \
                              --dosages_prefix chr${CHR}.tcga_normal_tissue \
                              --weights ../dbs/Prostate_Thibodeau.1MbpWindowSize.db \
                              --output_dir ../WindowSize_Predictions/chr${CHR}/ \
                              --samples ../Sample_Files/TCGA_Samples_With_Genotypes.samples

   bcftools annotate \
            --annotations ../dbSNP/All_20180423.vcf.gz \
            --columns ID \
            --output ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.rsid_annotated.vcf.gz \
            --output-type z \
            ../Genotypes/chr${CHR}.tcga_normal_tissue.dose.vcf.gz

   python2.7 scripts/PrediXcan.VCF.py --predict --chromosome ${CHR} \
                              --dosages ../Genotypes/ \
                              --dosages_prefix chr${CHR}.tcga_normal_tissue.dose.rsid_annotated \
                              --weights ../dbs/GTEx-V6p-HapMap-2016-09-08/TW_Prostate_0.5.db \
                              --output_dir ../GTEx_Predictions/chr${CHR}/ \
                              --samples ../Sample_Files/TCGA_Samples_With_Genotypes.samples \
                              --use_rsid

done
