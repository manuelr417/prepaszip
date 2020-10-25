#!/bin/sh
target=~/zips/UAGM
source=/home/ubuntu/git/PrepasGP/internal/cert/
while read p; do
  echo "GP-$p"
  echo $source
  file= source + "GP" + p + ".pdf"
  echo $file
done