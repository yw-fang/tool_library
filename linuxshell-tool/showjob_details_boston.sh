qstat -j $1 | grep cwd | gawk '{print $2}'
