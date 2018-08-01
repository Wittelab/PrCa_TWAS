for MATRIX_FILE in $(ls ../Glmnet_Inputs/*matrix)
do Rscript FitModels.R \
    --matrix ../../Glmnet_Inputs/${MATRIX_FILE} \
    --outdir ../LOOCV/ \
    --ncores 16 \
    --cv loocv
done
