cat comparison.chr1.onembp_vs_tcga.txt > allchrs.onembp_vs_tcga.txt
cat comparison.chr1.fivehundredkbp_vs_tcga.txt > allchrs.fivehundredkbp_vs_tcga.txt
cat comparison.chr1.fivehundredkbp_vs_onembp.txt > allchrs.fivehundredkbp_vs_onembp.txt

for CHR in {2..22};
do tail -n +2 comparison.chr${CHR}.onembp_vs_tcga.txt >> allchrs.onembp_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.fivehundredkbp_vs_tcga.txt >> allchrs.fivehundredkbp_vs_tcga.txt
   tail -n +2 comparison.chr${CHR}.fivehundredkbp_vs_onembp.txt >> allchrs.fivehundredkbp_vs_onembp.txt
done
