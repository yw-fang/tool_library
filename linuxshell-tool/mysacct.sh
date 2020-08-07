sacct command to monitor the running or finished jobs in Slurm job system
sacct -j $1 --format JobID,jobname,NTasks,nodelist,MaxRSS,MaxVMSize,AveRSS,AveVMSize
