#!/bin/bash

#this script was created by Yuewen Fang at CFM on Jan 26,2023. 
#the purpose is to see the information (CPUs, memory) of each node.
#  The CPUS(A/I/O/T) column in the output of the sinfo command shows the number of allocated, idle, other, and total CPUs on each node. 
partitions=("regular" "long" "xlong" "serial" "test" "large" "xlarge")

#mthod1, show information overview
# for partition in "${partitions[@]}"; do
#    echo "Partition: $partition"
#      echo "Nodes in partition: "
#        echo "Nodename      State"
#          sinfo -p $partition -h --format="%10N %8T" | grep -v "^$" 
# 	   echo ""
# 	   done

#method 2, show the node individually
 for partition in "${partitions[@]}"; do
  sinfo -N -p regular --format=%N,%C,%D,%t,%P,%m| awk -F"," '{available = $2 - $3; print $1 " " $2 " " $3 " " $4 " " $5 " " available " " $6}'
  echo "NODELIST CPUS(A/I/O/T) NODES STATE PARTITION 0 MEMORY"
done
