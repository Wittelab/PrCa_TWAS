# Usage: 
# Rscript CompareLOOCVand10Fold.R \
#         --loocv ../Mayo_Predictions/chr21/predicted_expression.txt \
#         --tenfold ../TenfoldCV_Predictions/chr21/predicted_expression.txt \
#         --tcga ../TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
#         --chromosome 21
#         --output_pre ./loocv_vs_tenfold.chr21

##########################
# INSTALL R DEPENDENCIES #
##########################

options(warn=-1)

cat("
###########################
Step 1: Installing Packages
###########################
\n")

packages    <- c("optparse")
uninstalled <- setdiff(packages, rownames(installed.packages()))
installed   <- setdiff(packages, uninstalled)
lapply(installed,require,character.only=TRUE)  

if ( length(uninstalled) != 0 ) {
  install.packages( uninstalled, repos="http://cran.r-project.org")
  lapply( uninstalled, require, character.only=TRUE )
}

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
    make_option(c("--loocv"), action="store_true",
                default=NA, type="character",
                help="Path to file containing imputed TCGA expression
                using the Mayo Clinic LOOCV reference panel."),
    make_option(c("--tenfold"), action="store_true",
                default=NA, type="character",
                help="Path to file containing imputed TCGA expression
                using the Mayo Clinic 10-fold cross-validation reference panel."),
    make_option(c("--tcga"), action="store_true",
                default=NA, type="character",
                help="Path to file containing observed TCGA expression."),
    make_option(c("--chromosome"), action="store_true",
                default=NA, type="character",
                help="Chromosome number to be analyzed."),
    make_option(c("--output_prefix"), action="store_true",
                default=NA, type="character",
                help="Path / prefix for output files comparing observed
                and imputed (via LOOCV, 10-fold) TCGA prostatic expression.")
  )
  parser   <- OptionParser(usage = "Rscript %prog [flag] value ...",
                         add_help_option=TRUE, option_list=option.list)
  cmd.args <- parse_args(parser, positional_arguments = FALSE)
  params   <- as.character(cmd.args)
}

params <- ParseArgs()

# Required input files
loocv_input <- params[1]
tenfold_input <- params[2]
tcga_input <- params[3]
chromosome <- params[4]
output_pre <- params[5]

if ( is.na(loocv_input) || is.na(tenfold_input) || is.na(tcga_input) || is.na(chromosome) || is.na(output_pre) )
{
  stop("Missing user inputs. Required inputs are '--loocv', '--tenfold', '--tcga', '--chromosome',
        \tand '--output_pre'. Refer to usage (-h flag) for additional inputs and arguments.")
}

#############################
# COMPARE EXPRESSION VALUES #
#############################

cat("
###################################
Step 3: Comparing Expression Values
###################################
\n")

# Read in TCGA Normal Expression; Set column and row names
# Input: "TCGA_Normal_Expression_Matrix.HGNC.txt"
tcga_normal = read.table(tcga_input, stringsAsFactors=F)
tcga_normal = t(tcga_normal)
colnames(tcga_normal) = tcga_normal[1, ]
tcga_normal = tcga_normal[-1, ]
rownames(tcga_normal) = tcga_normal[,1]
tcga_normal = tcga_normal[,-1]

tcga_normal = as.data.frame(tcga_normal, stringsAsFactors=F)

# Read in Mayo LOOCV Normal Expression; Set column and row names
loocv_tcga = read.table(loocv_input,stringsAsFactors=F)
colnames(loocv_tcga) = loocv_tcga[1, ]
loocv_tcga = loocv_tcga[-1, ]
rownames(loocv_tcga) = loocv_tcga[,1]
loocv_tcga = loocv_tcga[,-1]

# Reorder for consistency
loocv_tcga = loocv_tcga[match(rownames(tcga_normal), loocv_tcga$IID),]

# Read in Mayo 10-fold CV Normal Expression; Set column and row names
tenfold_tcga = read.table(tenfold_input,stringsAsFactors=F)
colnames(tenfold_tcga) = tenfold_tcga[1, ]
tenfold_tcga = tenfold_tcga[-1, ]
rownames(tenfold_tcga) = tenfold_tcga[,1]
tenfold_tcga = tenfold_tcga[,-1]

# Reorder for consistency
tenfold_tcga = tenfold_tcga[match(rownames(tcga_normal), tenfold_tcga$IID),]

genes_in_common = intersect(intersect(colnames(tenfold_tcga),colnames(loocv_tcga)), colnames(tcga_normal))

for( gene_name in genes_in_common ){

  expression_concat = data.frame(scale(as.numeric(tcga_normal[[gene_name]])), scale(as.numeric(loocv_tcga[[gene_name]])), scale(as.numeric(tenfold_tcga[[gene_name]])))
  colnames(expression_concat) = c("TCGA_NORMAL","LOOCV", "TENFOLD")

  if( length(unique(expression_concat$TCGA_NORMAL)) == 1 || length(unique(expression_concat$LOOCV)) == 1 || length(unique(expression_concat$TENFOLD)) == 1 ){
    print(paste("Skipping", gene_name, sep=" "))
    next
  }

  print(gene_name)

  results = glm(TCGA_NORMAL ~ TENFOLD, data = expression_concat)
  tenfold_vs_tcga_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$TCGA_NORMAL, expression_concat$TENFOLD, method="spearman")
  rho = spearman$estimate

  if( !exists("tenfold_vs_tcga") ){
    tenfold_vs_tcga = data.frame(gene=character(), spearmans_rho=double(), effect=double(), stderr=double(), pval=double(), mse=double())
    tenfold_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=tenfold_vs_tcga_model$coefficients[2,1], stderr=tenfold_vs_tcga_model$coefficients[2,2], pval=tenfold_vs_tcga_model$coefficients[2,4], mse=ssr)
    tenfold_vs_tcga = rbind(tenfold_vs_tcga, tenfold_vs_tcga_row)
  } else {
    tenfold_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=tenfold_vs_tcga_model$coefficients[2,1], stderr=tenfold_vs_tcga_model$coefficients[2,2], pval=tenfold_vs_tcga_model$coefficients[2,4], mse=ssr)
    tenfold_vs_tcga = rbind(tenfold_vs_tcga, tenfold_vs_tcga_row)
  }
  
  results = glm(TCGA_NORMAL ~ LOOCV, data = expression_concat)
  loocv_vs_tcga_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$TCGA_NORMAL, expression_concat$LOOCV, method="spearman")
  rho = spearman$estimate

  if( !exists("loocv_vs_tcga") ){
    loocv_vs_tcga = data.frame(gene=character(), spearmans_rho=double(), effect=double(), stderr=double(), pval=double(), mse=double())
    loocv_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=loocv_vs_tcga_model$coefficients[2,1], stderr=loocv_vs_tcga_model$coefficients[2,2], pval=loocv_vs_tcga_model$coefficients[2,4], mse=ssr)
    loocv_vs_tcga = rbind(loocv_vs_tcga, loocv_vs_tcga_row)
  } else {
    loocv_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=loocv_vs_tcga_model$coefficients[2,1], stderr=loocv_vs_tcga_model$coefficients[2,2], pval=loocv_vs_tcga_model$coefficients[2,4], mse=ssr)
    loocv_vs_tcga = rbind(loocv_vs_tcga, loocv_vs_tcga_row)
  }

  results = glm(LOOCV ~ TENFOLD, data = expression_concat)
  tenfold_vs_loocv_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$LOOCV, expression_concat$TENFOLD, method="spearman")
  rho = spearman$estimate

  if( !exists("tenfold_vs_loocv") ){
    tenfold_vs_loocv = data.frame(gene=character(), effect=double(), stderr=double(), pval=double(), mse=double())
    tenfold_vs_loocv_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=tenfold_vs_loocv_model$coefficients[2,1], stderr=tenfold_vs_loocv_model$coefficients[2,2], pval=tenfold_vs_loocv_model$coefficients[2,4], mse=ssr)
    tenfold_vs_loocv = rbind(tenfold_vs_loocv, tenfold_vs_loocv_row)
  } else {
    tenfold_vs_loocv_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=tenfold_vs_loocv_model$coefficients[2,1], stderr=tenfold_vs_loocv_model$coefficients[2,2], pval=tenfold_vs_loocv_model$coefficients[2,4], mse=ssr)
    tenfold_vs_loocv = rbind(tenfold_vs_loocv, tenfold_vs_loocv_row)
  }

}

write.table(tenfold_vs_tcga, file=paste(output_pre, "tenfold_vs_tcga", "txt", sep="."), row.names=F, quote=F, sep="\t")
write.table(loocv_vs_tcga, file=paste(output_pre, "loocv_vs_tcga", "txt", sep="."), row.names=F, quote=F, sep="\t")
write.table(tenfold_vs_loocv, file=paste(output_pre, "tenfold_vs_loocv", "txt", sep="."), row.names=F, quote=F, sep="\t")
