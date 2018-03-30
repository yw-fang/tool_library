#This script read the disp.yaml or disp_fc3.yaml or disp_fc2.yaml
#and print the distances
#Yue-Wen FANG, 2018 March 19th
#revision data: 2018 March 30th, add '-V' to fix some sort error
egrep '^\s+distance' $1|awk '{print $2}'|sort -V|uniq
