`Prostate_Thibodeau.db` --> The database we used in our study. 
                            Using dbGaP phs000985.v1.p1 dataset
                            Elastic Net model of variants (r2_info > 0.8)
                              within 500kb of gene boundaries
                            With model selection via LOOCV

`Prostate_Thibodeau.10foldCV.db` --> Same as above, except
                                     Model selection via 10-fold CV

`Prostate_Thibodeau.1MbpWindowSize.db` --> Again, using dbGaP phs000985.v1.p1 dataset
                                           Again, Elastic Net model of variants (r2_info > 0.8)
                                             within 1Mb of gene boundaries, vs. 500kb above

`TW_Prostate_0.5.db` --> GTEx v6p prostate tissue models
                         Downloaded from predictdb.org

`prostate_chrdb.pkl` --> Serialized .pkl file of gene --> chr
                           mapping for models in above file
