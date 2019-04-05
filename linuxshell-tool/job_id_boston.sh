#!/bin/bash
# This is used to print the working directory of the job in Boston cluster
# of Kyoto University
qstat -j $1 | grep cwd | gawk '{print $2}'
# Usage: job_id_boston.sh
