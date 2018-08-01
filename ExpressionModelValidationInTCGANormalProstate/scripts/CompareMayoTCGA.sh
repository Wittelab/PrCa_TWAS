cd ..

for CHR in {1..22};
do echo ${CHR};
  Rscript scripts/CompareMayoTCGA.R \
          --mayo Mayo_Predictions/chr${CHR}/predicted_expression.txt \
          --tcga TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
          --chromosome ${CHR} \
          --output_pre Mayo_Predictions/Parametric/comparison.chr${CHR} > Mayo_Predictions/Parametric/logs/chr${CHR}.log
done
