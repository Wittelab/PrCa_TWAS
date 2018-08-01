cat comparison.chr1.gtex_vs_tcga.txt > allchrs.gtex_vs_tcga.txt
cat comparison.chr1.mayo_vs_tcga.txt > allchrs.mayo_vs_tcga.txt
cat comparison.chr1.mayo_vs_gtex.txt > allchrs.mayo_vs_gtex.txt

for CHR in {2..22};
do tail -n +2 comparison.chr${CHR}.gtex_vs_tcga.txt >> allchrs.gtex_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.mayo_vs_tcga.txt >> allchrs.mayo_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.mayo_vs_gtex.txt >> allchrs.mayo_vs_gtex.txt
done
