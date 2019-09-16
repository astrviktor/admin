#!/bin/bash

# make mail file

sudo echo "To: kotemail@rambler.ru" > /home/pi/stata.txt
sudo echo "From: homestata@yandex.ru" | sudo tee -a /home/pi/stata.txt
sudo echo "Subject: statistica" | sudo tee -a /home/pi/stata.txt
sudo echo "" | sudo tee -a /home/pi/stata.txt

# speedtest

sudo echo "speedtest" | sudo tee -a /home/pi/stata.txt
sudo date +%Y-%m-%d" "%H-%M-%S | sudo tee -a /home/pi/stata.txt
sudo speedtest | grep -e Hosted -e Download -e Upload | sudo tee -a /home/pi/stata.txt
sudo echo "" | sudo tee -a /home/pi/stata.txt

# iperf

sudo echo "iperf" | sudo tee -a /home/pi/stata.txt
sudo date +%Y-%m-%d" "%H-%M-%S | sudo tee -a /home/pi/stata.txt
#sudo iperf -c 192.168.99.250 --num 20M --reportstyle C | sudo tee -a /home/pi/stata.txt
sudo iperf -c 192.168.99.250 --num 20M | grep -e MBytes | sudo tee -a /home/pi/stata.txt
sudo echo "" | sudo tee -a /home/pi/stata.txt

# discs

sudo echo "disks" | sudo tee -a /home/pi/stata.txt
sudo date +%Y-%m-%d" "%H-%M-%S | sudo tee -a /home/pi/stata.txt
sudo df -h | grep -e root -e media | sudo tee -a /home/pi/stata.txt
sudo echo "" | sudo tee -a /home/pi/stata.txt


# send mail

sudo ssmtp kotemail@rambler.ru < /home/pi/stata.txt

