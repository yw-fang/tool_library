#!/bin/bash
#author: Y.-W.FANG
#purpose: list all the q grid points for phono3py
grep '\-\ grid_point' ir_grid_points.yaml   | gawk '{printf("%d,",$3)}'

#In the homepage of phono3py, Togo-sensei showed his command which you can also use
#egrep '^- grid_point:' ir_grid_points.yaml|awk '{printf("%d,",$3)}'


