###########################################

from datetime import datetime

datenow = datetime.now().date().strftime('%Y-%m-%d')
timenow = datetime.now().time().strftime('%H:%M')

filename = str(datenow) + '.csv'

# print(datenow)
# print(timenow)
# print(filename)

##########################################

import subprocess

# cmd = 'speedtest'

cmd = 'speedtest'
out = subprocess.Popen(cmd.split(' '),
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)

stdout,stderr = out.communicate()

#print(stderr)

speedtest_out = stdout.splitlines()

speedtest_download = str(speedtest_out[-3])
speedtest_upload = str(speedtest_out[-1])

#print(speedtest_download)
#print(speedtest_upload)
try:
	speedtest_download_speed = float(speedtest_download.split(' ')[-2])
	speedtest_upload_speed = float(speedtest_upload.split(' ')[-2])
except ValueError:
	speedtest_download_speed = 0.0
	speedtest_upload_speed = 0.0

speedtest_err = stderr

#print(speedtest_download_speed)
#print(speedtest_upload_speed)

###############################################################

# cmd = 'sudo iperf -c 192.168.99.250 --num 10M --reportstyle C'

cmd = 'sudo iperf -c 192.168.99.250 --num 10M --reportstyle C'
out = subprocess.Popen(cmd.split(' '),
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)

stdout,stderr = out.communicate()

#print(stderr)

wifi_speed_str = str(stdout)

try:
	wifi_speed = float(wifi_speed_str.split(',')[-1]) / 1e6
	wifi_speed = round(wifi_speed, 2)
except ValueError:
	wifi_speed = 0.0


#print(stdout)
#print(wifi_speed)

###############################################################

print(filename)

print(datenow)
print(timenow)

print(speedtest_download_speed)
print(speedtest_upload_speed)

print(wifi_speed)

###############################################################

# make data

import pandas as pd

data = [ (datenow, timenow, speedtest_download_speed, speedtest_upload_speed, wifi_speed) ]
df_data = pd.DataFrame(data, columns = ['Date' , 'Time', 'Download' , 'Upload', 'Wifi'])

###############################################################

import os

path = '/var/log/speedstat/'

if os.path.exists(path + filename):
	print('yes')
	speedstat = pd.read_csv(path + filename)
	speedstat = speedstat.append(df_data, ignore_index=True)
	speedstat.to_csv(path + filename, index=False)
else:
	print('no')
	speedstat = df_data
	speedstat.to_csv(path + filename, index=False)
