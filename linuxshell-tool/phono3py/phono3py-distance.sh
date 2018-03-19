#This script read the disp.yaml or disp_fc3.yaml or disp_fc2.yaml
#and print the distances
#Yue-Wen FANG, 2018 March 19th
egrep '^\s+distance' $1|awk '{print $2}'|sort|uniq
