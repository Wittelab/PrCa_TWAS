for INDEX in {1..1884}
do GENE=$(head -$INDEX Genes_in_both_GTEx_and_Mayo.txt | tail -1)
  Rscript FitModels.R \
    --matrix ../../Glmnet_Inputs/${GENE}.matrix \
    --outdir ../Tenfold/ \
    --ncores 16 \
    --cv tenfold
done
