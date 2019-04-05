#!/bin/bash
# This is used to print the working directory of the job in Boston cluster
# of Kyoto University
qstat -j $1 | grep cwd | gawk '{print $2}'
# Usage: showjob_details_boston.sh job-ID
