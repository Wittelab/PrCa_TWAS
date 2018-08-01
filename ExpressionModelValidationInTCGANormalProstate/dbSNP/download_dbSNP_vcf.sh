wget ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/All_20180423.vcf.gz
# Next, to avoid "index created earlier than target file" error:
touch All_20180423.vcf.gz.tbi
