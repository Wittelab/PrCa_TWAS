for MATRIX_FILE in $(ls ../../Glmnet_Inputs/1MbpWindow/*matrix)
do Rscript FitModels.R \
    --matrix ../../Glmnet_Inputs/1MbpWindow/${MATRIX_FILE} \
    --outdir ../1MbpWindow/ \
    --ncores 16 \
    --cv loocv
done
