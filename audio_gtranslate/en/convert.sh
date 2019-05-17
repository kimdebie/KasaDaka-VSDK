#!/bin/bash 
if [ ! -d converted/ ] 
then 
 mkdir converted; 
fi;
for i in ./*.mp3
 do sox -S "$i" -r 8k -b 16 -c 1 -e signed-integer "converted/$(basename -s .mp3 "$i").wav";
done;
