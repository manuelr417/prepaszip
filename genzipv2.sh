#!/bin/bash
INPUT=UAGM.cvs
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read flname gp
do
  name="GP-"$gp
	echo "GP : $gp"
	echo "NAME : $name"
done < $INPUT
IFS=$OLDIFS