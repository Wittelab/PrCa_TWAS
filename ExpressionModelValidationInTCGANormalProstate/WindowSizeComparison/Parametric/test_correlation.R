onembp = read.table("allchrs.onembp_vs_tcga.txt",header=T)
fivekbp = read.table("allchrs.fivehundredkbp_vs_tcga.txt",header=T)
t.test(onembp$effect, fivekbp$effect)

#         Welch Two Sample t-test
# 
# data:  onembp$effect and fivekbp$effect
# t = 0.023273, df = 246, p-value = 0.9815
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#  -0.04733509  0.04846705
# sample estimates:
#  mean of x  mean of y 
# 0.08423333 0.08366735 

cor.test(onembp$effect, fivekbp$effect)

#         Pearson's product-moment correlation
# 
# data:  onembp$effect and fivekbp$effect
# t = 25.605, df = 122, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.8852058 0.9420189
# sample estimates:
#       cor 
# 0.9182113 

mean(onembp$effect)   
# [1] 0.08423333
mean(fivekbp$effect)
# [1] 0.08366735

t.test(onembp$mse, fivekbp$mse)

#         Welch Two Sample t-test
# 
# data:  onembp$mse and fivekbp$mse
# t = -0.031902, df = 245.85, p-value = 0.9746
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#  -0.7727954  0.7481609
# sample estimates:
# mean of x mean of y 
#  42.08330  42.09562 

cor.test(onembp$mse, fivekbp$mse)

#         Pearson's product-moment correlation
# 
# data:  onembp$mse and fivekbp$mse
# t = 33.188, df = 122, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.9277154 0.9638929
# sample estimates:
#       cor 
# 0.9488303 

mean(onembp$mse)
# [1] 42.0833
mean(fivekbp$mse)
# [1] 42.09562
