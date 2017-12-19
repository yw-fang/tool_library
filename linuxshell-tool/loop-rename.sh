#!/bin/bash

for((i=360;i>=0;i=i-15));
do
  mv theta-$i alpha-$i
done
