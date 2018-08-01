cat comparison.chr1.all_mayo_vs_tcga.txt > allchrs.all_mayo_vs_tcga.txt

for CHR in {2..22};
do tail -n +2 comparison.chr${CHR}.all_mayo_vs_tcga.txt >> allchrs.all_mayo_vs_tcga.txt
done
