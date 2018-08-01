cat comparison.chr1.loocv_vs_tcga.txt > allchrs.loocv_vs_tcga.txt
cat comparison.chr1.tenfold_vs_tcga.txt > allchrs.tenfold_vs_tcga.txt
cat comparison.chr1.tenfold_vs_loocv.txt > allchrs.tenfold_vs_loocv.txt

for CHR in {2..22};
do tail -n +2 comparison.chr${CHR}.loocv_vs_tcga.txt >> allchrs.loocv_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.tenfold_vs_tcga.txt >> allchrs.tenfold_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.tenfold_vs_loocv.txt >> allchrs.tenfold_vs_loocv.txt
done
