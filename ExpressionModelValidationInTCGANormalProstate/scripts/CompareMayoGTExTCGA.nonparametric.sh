cd ..

for CHR in {1..22};
do echo ${CHR};
  Rscript scripts/CompareMayoGTExTCGA.nonparametric.R \
          --gtex GTEx_Predictions/chr${CHR}/predicted_expression.txt \
          --mayo Mayo_Predictions/chr${CHR}/predicted_expression.txt \
          --tcga TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
          --chromosome ${CHR} \
          --output_pre ExpressionComparisons/Nonparametric/comparison.chr${CHR} > ExpressionComparisons/Nonparametric/logs/chr${CHR}.log
done
