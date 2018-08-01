cd /wittelab/data2/emamin/TWAS/ReviewerResponses/MAF_Lookup

for QUERYCHR in {1..22};
do echo "$QUERYCHR"
   for SNPID in $(sqlite3 ../TCGAImputation/dbs/Prostate_Thibodeau.db < <(echo "SELECT rsid FROM weights WHERE rsid LIKE \"chr${QUERYCHR}.%\";"));
   do CHR=$(echo "$SNPID" | cut -d"." -f1 | cut -d"r" -f2);
      POS=$(echo "$SNPID" | cut -d"." -f2);
      # TBXSTRING=$(tabix HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz $CHR:$POS-$POS)
      echo -e "$CHR\t$POS\t$POS\t$SNPID"
   done | sort -gk2,2 | uniq > chr${QUERYCHR}.bed.txt
   tabix -R chr${QUERYCHR}.bed.txt HRC.r1-1.GRCh37.wgs.mac5.sites.tab.gz $CHR:$POS-$POS > chr${QUERYCHR}.tabix_out.txt
done
