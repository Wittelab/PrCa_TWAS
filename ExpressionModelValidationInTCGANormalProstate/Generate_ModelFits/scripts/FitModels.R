##########################
# INSTALL R DEPENDENCIES #
##########################

options(warn=-1)
'%notin%' <- Negate('%in%')

cat("
###########################
Step 1: Installing Packages
###########################
\n")

### NOTE: may need to add "lib.loc" parameter for lapply-require cmd
lapply( c("iterators", "foreach", "optparse", "glmnet", "doMC", "methods"), require,
        character.only=TRUE )

########################
# PARSE USER ARGUMENTS #
########################

cat("
#########################
Step 2: Parsing Arguments
#########################
\n")

ParseArgs <- function()
{
  option.list <- list(
    make_option(c("--matrix"), action="store_true",
                default=NA, type="character",
                help="File name for input eQTL matrix."),
    make_option(c("--outdir"), action="store_true",
                default=NA, type="character",
                help="Path to output directory."),
    make_option(c("--ncores"), action="store_true",
                default=NA, type="character",
                help="Number of VM CPUs."),
    make_option(c("--cv"), action="store_true",
                default=NA, type="character",
                help="Cross-validation procedure (options: 'tenfold', 'loocv').")
    )
  parser   <- OptionParser(usage = "Rscript %prog [flag] value ...",
                         add_help_option=TRUE, option_list=option.list)
  cmd.args <- parse_args(parser, positional_arguments = FALSE)
  params   <- as.character(cmd.args)
}

params <- ParseArgs()

# Required input files
input.file <- params[1]
output.dir <- params[2]
n.cores    <- params[3]
cv         <- params[4]


if ( is.na(input.file) || is.na(n.cores) || is.na(cv) || cv %notin% c("tenfold", "loocv") )
{
  stop("Missing user inputs. Required inputs are '--matrix', '--ncores', and
        \t'--cv'. Refer to usage (-h flag) for additional details.")
}

######################
# PLOTTING FUNCTIONS #
######################

cat("
####################################
Step 3: Regress and Generate Outputs
####################################
\n")

registerDoMC(cores=n.cores)

geneMatrix <- read.table(input.file, header=TRUE, row.names=1)

geneFile         <- strsplit(input.file,".", fixed=TRUE)[[1]][1]
geneNameElements <- strsplit(geneFile,"/", fixed=TRUE)[[1]]
geneName         <- geneNameElements[length(geneNameElements)]

# If the matrix dimensions are too small, don't even run the models
if( dim(geneMatrix)[2] < 3 ){
  print(paste("No SNPs/variants provided for",geneName,"-- exiting",sep=" "))
} else {
# Otherwise, run the desired GLMNet models
  models <- c("ridge","enet","lasso")
  for(i in 1:1) {
    alpha <- i/2
    model <- models[i+1]
    fit <- glmnet(
                  as.matrix(geneMatrix[,1:dim(geneMatrix)[2]-1]),
                  as.matrix(geneMatrix[,dim(geneMatrix)[2]]),
                  alpha=alpha
                 )
    vnat <- coef(fit)
    vnat <- vnat[-1,ncol(vnat)]
    xvars <- c("dev", "lambda", "norm")
    for(j in 0:2) {
      # Plot beta values
      xvar <- xvars[j+1]
      output.file <- paste(geneName, model, xvar, "png", sep=".")
      output.file <- paste(output.dir, output.file, sep="/")
      png(filename = output.file, width = 800, height = 600)

      plot(fit, xvar=xvar, label=FALSE)
      axis(4, at=vnat, line=-8, 
           label=colnames(geneMatrix)[1:dim(geneMatrix)[2]-1],
           tick=FALSE, cex.axis=1, las=1)

      dev.off()
    }

    # Either 10-fold or L.O.O. Cross Validation
    cvfolds = "tenfold"
    if( cv == "loocv" ){
      cvfolds = dim(geneMatrix)[1]
    }

    cv.fit <- cv.glmnet(
                        as.matrix(geneMatrix[,1:dim(geneMatrix)[2]-1]),
                        as.matrix(geneMatrix[,dim(geneMatrix)[2]]),
                        alpha=alpha, type.measure = "mse", 
		        nfolds=cvfolds, parallel = TRUE
                       )
    
    print(model)
    print(cv.fit$lambda.min)
    gene.pred <- predict(cv.fit, s='lambda.min',
                         newx=as.matrix(geneMatrix[,1:dim(geneMatrix)[2]-1]))
    true.vs.pred <- cbind(y_true = as.matrix(geneMatrix[,dim(geneMatrix)[2]]),
                          y_pred = gene.pred)
    rsq <- boot::corr(d=true.vs.pred) ^ 2
    if( !(rsq == Inf || rsq == "NaN") ){
      # Plot cross validation trace
      output.file <- paste(geneName, model, "cvtrace", "png", sep=".")
      output.file <- paste(output.dir, output.file, sep="/")
      png(filename = output.file, width = 800, height = 600)
      plot(cv.fit)
      dev.off()
      # Write nonzero coefficients to table
      output.file <- paste(geneName, model, "betas", "txt", sep=".")
      output.file <- paste(output.dir, output.file, sep="/")
      nonzero.indices <- which(coef(cv.fit,s="lambda.min") != 0)
      nonzero.betas <- coef(cv.fit, s="lambda.min")[nonzero.indices,]
      nonintercept.betas <- nonzero.betas[2:length(nonzero.betas)]
      print(paste(length(nonintercept.betas),"nonzero betas", sep=" "))
      print(output.file)
      write.table(nonintercept.betas, output.file, quote=FALSE, 
                  col.names=FALSE, sep="\t")
      cat(paste("r2: ", rsq, "\n", sep=""), file=output.file, append=TRUE)
    }
  }
}

cat("
########
# Fin! #
########
\n")
