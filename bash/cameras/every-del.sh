#!/bin/bash

# block 01

ydated=`date --date="3 days ago" +%Y%m%d`
echo $ydated

cd /media/CAMERA_01
rm -rf $ydated

# block 02

ydated=`date --date="4 days ago" +%Y%m%d`
echo $ydated

cd /media/CAMERA_02
rm -rf $ydated

# block 03

ydated=`date --date="4 days ago" +%Y%m%d`
echo $ydated

cd /media/CAMERA_03
rm -rf $ydated

# block 04

ydated=`date --date="4 days ago" +%Y%m%d`
echo $ydated

cd /media/CAMERA_04
rm -rf $ydated

# block 05

ydated=`date --date="4 days ago" +%Y%m%d`
echo $ydated

cd /media/CAMERA_05
rm -rf $ydated

