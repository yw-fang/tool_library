# List all the files in the current directory to .log file
find . > archive-"$(date +"%Y_%m_%d_%I_%M_%p")".log
