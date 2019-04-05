#!/bin/bash
# This is used to print the working directory of the job in Boston cluster
# of Kyoto University
# Usage: jobs_boston.sh

jobid=$(qstat | grep ywfang | gawk '{print $1}')  # pass the all job-IDs to jobid
for i in $jobid:
do
echo $i
qstat -j $i | grep cwd | gawk '{print $2}'  # print working directory in the SGE submission system
done
