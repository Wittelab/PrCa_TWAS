Scripts and output data for fitting models using `../Glmnet_Inputs/` data generated from dbGaP training dataset (phs000985.v1.p1)

`1MbpWindow` --> Contains beta files (modeled variants with nonzero effect estimates, + cross-validated model r2)
                 These were used to populate the `Prostate_Thibodeau.1MbpWindowSize.db` database.

`LOOCV` --> Contains beta files (modeled variants with nonzero effect estimates, + cross-validated model r2)
            These were used to populate the `Prostate_Thibodeau.db` database.

`Tenfold` --> Contains beta files (modeled variants with nonzero effect estimates, + cross-validated model r2)
              These were used to populate the `Prostate_Thibodeau.10foldCV.db` database.

`scripts` --> shell/R scripts necessary to generate the beta files described above
