#!bin/bash
#author: Y.-W.FANG
grep '\-\ grid_point' ir_grid_points.yaml   | gawk '{printf("%d,",$3)}'

#In the homepage of phono3py, Togo-sensei showed his command which you can also use
#egrep '^- grid_point:' ir_grid_points.yaml|awk '{printf("%d,",$3)}'


