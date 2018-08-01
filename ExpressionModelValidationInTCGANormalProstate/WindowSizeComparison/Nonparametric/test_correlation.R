onembp = read.table("allchrs.onembp_vs_tcga.txt",header=T)
fivekbp = read.table("allchrs.fivehundredkbp_vs_tcga.txt",header=T)
t.test(onembp$spearmans_rho, fivekbp$spearmans_rho)
wilcox.test(onembp$spearmans_rho, fivekbp$spearmans_rho)

#         Welch Two Sample t-test
# 
# data:  onembp$spearmans_rho and fivekbp$spearmans_rho
# t = 0.13569, df = 245.96, p-value = 0.8922
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#  -0.04615815  0.05298854
# sample estimates:
#  mean of x  mean of y 
# 0.09388819 0.09047299

cor.test(onembp$spearmans_rho, fivekbp$spearmans_rho)
cor.test(onembp$spearmans_rho, fivekbp$spearmans_rho, method="spearman")

#         Pearson's product-moment correlation
# 
# data:  onembp$spearmans_rho and fivekbp$spearmans_rho
# t = 20.778, df = 122, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.8369786 0.9166040
# sample estimates:
#       cor 
# 0.8829896

mean(onembp$spearmans_rho)
# [1] 0.09388819
mean(fivekbp$spearmans_rho)
# [1] 0.09047299
