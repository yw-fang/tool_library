#for i in {seq 20,120,20}
#for((i=20, i<=120,i++));
for((i=20;i<=120;i=i+20));  
do 
  echo $i;
  echo 'PSTRESS   = '$i >> ./hello.txt
done


for((i=0;i<=10;i=i+1));  
do 
  echo $i;
  echo 'PSTRESS   = '$i >> ./hello.txt
done
