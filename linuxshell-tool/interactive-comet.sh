#Lauch a interactive session on Comet. 
#Author:Yue-Wen FANG at 2018 July 7th
srun --partition=shared --pty --nodes=1 --ntasks-per-node=20 -t 00:60:00 --wait=0 --export=ALL /bin/bash
