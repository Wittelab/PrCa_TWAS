# Usage: 
# /wittelab/data1/software/R-3.2.2/bin/Rscript Compare1MBand500KB.R \
#                                              --onembp ../WindowSize_Predictions/chr21/predicted_expression.txt \
#                                              --fivehundkbp ../LOOCV_Predictions/chr21/predicted_expression.txt \
#                                              --tcga ../TCGA_ObservedNormalExpression/TCGA_Normal_Expression_Matrix.HGNC.txt \
#                                              --chromosome 21
#                                              --output_pre ./1Mbp_vs_500Kbp.chr21

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
    make_option(c("--onembp"), action="store_true",
                default=NA, type="character",
                help="Path to file containing imputed TCGA expression
                using the Mayo Clinic 1Mbp window LOOCV reference panel."),
    make_option(c("--fivehundkbp"), action="store_true",
                default=NA, type="character",
                help="Path to file containing imputed TCGA expression
                using the Mayo Clinic 500Kbp window LOOCV reference panel."),
    make_option(c("--tcga"), action="store_true",
                default=NA, type="character",
                help="Path to file containing observed TCGA expression."),
    make_option(c("--chromosome"), action="store_true",
                default=NA, type="character",
                help="Chromosome number to be analyzed."),
    make_option(c("--output_prefix"), action="store_true",
                default=NA, type="character",
                help="Path / prefix for output files comparing observed
                and imputed (via 1Mbp vs. 500Kbp LOOCV) TCGA prostatic expression.")
  )
  parser   <- OptionParser(usage = "Rscript %prog [flag] value ...",
                         add_help_option=TRUE, option_list=option.list)
  cmd.args <- parse_args(parser, positional_arguments = FALSE)
  params   <- as.character(cmd.args)
}

params <- ParseArgs()

# Required input files
one_mbp_input <- params[1]
fivehundred_kbp_input <- params[2]
tcga_input <- params[3]
chromosome <- params[4]
output_pre <- params[5]

if ( is.na(one_mbp_input) || is.na(fivehundred_kbp_input) || is.na(tcga_input) || is.na(chromosome) || is.na(output_pre) )
{
  stop("Missing user inputs. Required inputs are '--onembp', '--fivehundkbp', '--tcga', '--chromosome',
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

# setwd("/Volumes/VaultN/Documents/Research/TWAS/TCGA_NormalTissueExpression/FPKM_for_Genotyped_Subjects/")

# Read in TCGA Normal Expression; Set column and row names
# Input: "TCGA_Normal_Expression_Matrix.HGNC.txt"
tcga_normal = read.table(tcga_input, stringsAsFactors=F)
tcga_normal = t(tcga_normal)
colnames(tcga_normal) = tcga_normal[1, ]
tcga_normal = tcga_normal[-1, ]
rownames(tcga_normal) = tcga_normal[,1]
tcga_normal = tcga_normal[,-1]

tcga_normal = as.data.frame(tcga_normal, stringsAsFactors=F)

# Read in Mayo 1Mbp onembp Normal Expression; Set column and row names
onembp_tcga = read.table(one_mbp_input,stringsAsFactors=F)
colnames(onembp_tcga) = onembp_tcga[1, ]
onembp_tcga = onembp_tcga[-1, ]
rownames(onembp_tcga) = onembp_tcga[,1]
onembp_tcga = onembp_tcga[,-1]

# Reorder for consistency
onembp_tcga = onembp_tcga[match(rownames(tcga_normal), onembp_tcga$IID),]

# Read in Mayo 500Kbp onembp Normal Expression; Set column and row names
fivehundredkbp_tcga = read.table(fivehundred_kbp_input,stringsAsFactors=F)
colnames(fivehundredkbp_tcga) = fivehundredkbp_tcga[1, ]
fivehundredkbp_tcga = fivehundredkbp_tcga[-1, ]
rownames(fivehundredkbp_tcga) = fivehundredkbp_tcga[,1]
fivehundredkbp_tcga = fivehundredkbp_tcga[,-1]

# Reorder for consistency
fivehundredkbp_tcga = fivehundredkbp_tcga[match(rownames(tcga_normal), fivehundredkbp_tcga$IID),]

genes_in_common = intersect(intersect(colnames(fivehundredkbp_tcga),colnames(onembp_tcga)), colnames(tcga_normal))

for( gene_name in genes_in_common ){

  expression_concat = data.frame(scale(as.numeric(tcga_normal[[gene_name]])), scale(as.numeric(onembp_tcga[[gene_name]])), scale(as.numeric(fivehundredkbp_tcga[[gene_name]])))
  colnames(expression_concat) = c("TCGA_NORMAL","onembp", "fivehundredkbp")

  if( length(unique(expression_concat$TCGA_NORMAL)) == 1 || length(unique(expression_concat$onembp)) == 1 || length(unique(expression_concat$fivehundredkbp)) == 1 ){
    print(paste("Skipping", gene_name, sep=" "))
    next
  }

  print(gene_name)

  results = glm(TCGA_NORMAL ~ fivehundredkbp, data = expression_concat)
  fivehundredkbp_vs_tcga_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$TCGA_NORMAL, expression_concat$fivehundredkbp, method="spearman")
  rho = spearman$estimate

  if( !exists("fivehundredkbp_vs_tcga") ){
    fivehundredkbp_vs_tcga = data.frame(gene=character(), spearmans_rho=double(), effect=double(), stderr=double(), pval=double(), mse=double())
    fivehundredkbp_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=fivehundredkbp_vs_tcga_model$coefficients[2,1], stderr=fivehundredkbp_vs_tcga_model$coefficients[2,2], pval=fivehundredkbp_vs_tcga_model$coefficients[2,4], mse=ssr)
    fivehundredkbp_vs_tcga = rbind(fivehundredkbp_vs_tcga, fivehundredkbp_vs_tcga_row)
  } else {
    fivehundredkbp_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=fivehundredkbp_vs_tcga_model$coefficients[2,1], stderr=fivehundredkbp_vs_tcga_model$coefficients[2,2], pval=fivehundredkbp_vs_tcga_model$coefficients[2,4], mse=ssr)
    fivehundredkbp_vs_tcga = rbind(fivehundredkbp_vs_tcga, fivehundredkbp_vs_tcga_row)
  }
  
  results = glm(TCGA_NORMAL ~ onembp, data = expression_concat)
  onembp_vs_tcga_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$TCGA_NORMAL, expression_concat$onembp, method="spearman")
  rho = spearman$estimate

  if( !exists("onembp_vs_tcga") ){
    onembp_vs_tcga = data.frame(gene=character(), spearmans_rho=double(), effect=double(), stderr=double(), pval=double(), mse=double())
    onembp_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=onembp_vs_tcga_model$coefficients[2,1], stderr=onembp_vs_tcga_model$coefficients[2,2], pval=onembp_vs_tcga_model$coefficients[2,4], mse=ssr)
    onembp_vs_tcga = rbind(onembp_vs_tcga, onembp_vs_tcga_row)
  } else {
    onembp_vs_tcga_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=onembp_vs_tcga_model$coefficients[2,1], stderr=onembp_vs_tcga_model$coefficients[2,2], pval=onembp_vs_tcga_model$coefficients[2,4], mse=ssr)
    onembp_vs_tcga = rbind(onembp_vs_tcga, onembp_vs_tcga_row)
  }

  results = glm(onembp ~ fivehundredkbp, data = expression_concat)
  fivehundredkbp_vs_onembp_model = summary(results)
  ssr = sum(residuals(results)^2)

  spearman = cor.test(expression_concat$onembp, expression_concat$fivehundredkbp, method="spearman")
  rho = spearman$estimate

  if( !exists("fivehundredkbp_vs_onembp") ){
    fivehundredkbp_vs_onembp = data.frame(gene=character(), effect=double(), stderr=double(), pval=double(), mse=double())
    fivehundredkbp_vs_onembp_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=fivehundredkbp_vs_onembp_model$coefficients[2,1], stderr=fivehundredkbp_vs_onembp_model$coefficients[2,2], pval=fivehundredkbp_vs_onembp_model$coefficients[2,4], mse=ssr)
    fivehundredkbp_vs_onembp = rbind(fivehundredkbp_vs_onembp, fivehundredkbp_vs_onembp_row)
  } else {
    fivehundredkbp_vs_onembp_row = data.frame(gene=as.character(gene_name), spearmans_rho=rho, effect=fivehundredkbp_vs_onembp_model$coefficients[2,1], stderr=fivehundredkbp_vs_onembp_model$coefficients[2,2], pval=fivehundredkbp_vs_onembp_model$coefficients[2,4], mse=ssr)
    fivehundredkbp_vs_onembp = rbind(fivehundredkbp_vs_onembp, fivehundredkbp_vs_onembp_row)
  }

}

write.table(fivehundredkbp_vs_tcga, file=paste(output_pre, "fivehundredkbp_vs_tcga", "txt", sep="."), row.names=F, quote=F, sep="\t")
write.table(onembp_vs_tcga, file=paste(output_pre, "onembp_vs_tcga", "txt", sep="."), row.names=F, quote=F, sep="\t")
write.table(fivehundredkbp_vs_onembp, file=paste(output_pre, "fivehundredkbp_vs_onembp", "txt", sep="."), row.names=F, quote=F, sep="\t")
