#!/bin/bash

ydated=`date '+%Y%m%d' -d yesterday`
ydated_file=$ydated'*.avi'

# block 01

cd /media/CAMERA_01

findf=$(ls $ydated_file)
echo $findf

if [ $findf = ""]
then
  # if no files to work then exit
  echo "No files for work"
else
  # if yes files to work then work

  mkdir $ydated

  mv $ydated_file $ydated
  echo "moving files"
fi

# block 02

cd /media/CAMERA_02

findf=$(ls $ydated_file)
echo $findf

if [ $findf = ""]
then
  # if no files to work then exit
  echo "No files for work"
else
  # if yes files to work then work

  mkdir $ydated

  mv $ydated_file $ydated
  echo "moving files"
fi

# block 03

cd /media/CAMERA_03

findf=$(ls $ydated_file)
echo $findf

if [ $findf = ""]
then
  # if no files to work then exit
  echo "No files for work"
else
  # if yes files to work then work

  mkdir $ydated

  mv $ydated_file $ydated
  echo "moving files"
fi

# block 04

cd /media/CAMERA_04

findf=$(ls $ydated_file)
echo $findf

if [ $findf = ""]
then
  # if no files to work then exit
  echo "No files for work"
else
  # if yes files to work then work

  mkdir $ydated

  mv $ydated_file $ydated
  echo "moving files"
fi

# block 05

cd /media/CAMERA_05

findf=$(ls $ydated_file)
echo $findf

if [ $findf = ""]
then
  # if no files to work then exit
  echo "No files for work"
else
  # if yes files to work then work

  mkdir $ydated

  mv $ydated_file $ydated
  echo "moving files"
fi

