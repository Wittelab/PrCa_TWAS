cd ..

for CHR in {1..22};
do echo ${CHR};
  Rscript scripts/CompareLOOCVand10Fold.R \
          --loocv Mayo_Predictions/chr${CHR}/predicted_expression.txt \
          --tenfold TenfoldCV_Predictions/chr${CHR}/predicted_expression.txt \
          --tcga TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
          --chromosome ${CHR} \
          --output_pre LOOCVand10FoldComparison/comparison.chr${CHR};
done
