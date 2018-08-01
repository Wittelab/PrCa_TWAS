cd /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/
mkdir /wittelab/data2/emamin/TWAS/ReviewerResponses/TCGAImputation/WindowSizeComparison/Parametric/

for CHR in {1..22};
do echo ${CHR};
  /wittelab/data1/software/R-3.2.2/bin/Rscript scripts/Compare1MBand500KB.R \
                                             --onembp WindowSize_Predictions/chr${CHR}/predicted_expression.txt \
                                             --fivehundkbp Mayo_Predictions/chr${CHR}/predicted_expression.txt \
                                             --tcga TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
                                             --chromosome ${CHR} \
                                             --output_pre WindowSizeComparison/Parametric/comparison.chr${CHR} > WindowSizeComparison/Parametric/comparison.chr${CHR}.log
done
