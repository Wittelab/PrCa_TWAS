cd ..

for CHR in {1..22};
do echo ${CHR};
  Rscript scripts/CompareMayoTCGA.nonparametric.R \
          --mayo Mayo_Predictions/chr${CHR}/predicted_expression.txt \
          --tcga TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
          --chromosome ${CHR} \
          --output_pre Mayo_Predictions/Nonparametric/comparison.chr${CHR} > Mayo_Predictions/Nonparametric/chr${CHR}.log
done
