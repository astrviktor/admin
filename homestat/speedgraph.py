from datetime import date, timedelta

date_today = date.today()

date_yesterday = date_today - timedelta(days=1)

date_today = date_today.strftime('%Y-%m-%d')
date_yesterday = date_yesterday.strftime('%Y-%m-%d')

###############################################################

import pandas as pd


path = '/var/log/speedstat/'

yesterday = pd.read_csv(path + str(date_yesterday) + '.csv')
today = pd.read_csv(path + str(date_today) + '.csv')

###############################################################

def float_time(time):
    return float(time[0:2]) + float(time[3:]) / 60

yesterday["TimeFloat"] = yesterday["Time"].apply(lambda t: float_time(t))
today["TimeFloat"] = today["Time"].apply(lambda t: float_time(t))

###############################################################

timeline = []
for i in range(25):
    timeline = timeline + [i]

dataline = []
for i in range(19):
    dataline = dataline + [i]

###############################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 6))
ax = fig.add_subplot(111)
ax.plot(yesterday['TimeFloat'], yesterday['Download'], 'deeppink', label='Download')
ax.plot(yesterday['TimeFloat'], yesterday['Upload'], 'purple', label='Upload')
ax.plot(yesterday['TimeFloat'], yesterday['Wifi'], 'royalblue', label='Wifi')
ax.set_xticks(timeline)
ax.set_yticks(dataline)
ax.set_ylabel('Speed, Mbit')
ax.set_title(str(date_yesterday))
ax.grid(True)
ax.legend(loc='lower left')
fig.savefig(path + str(date_yesterday) + '.png', dpi=100, bbox_inches='tight', pad_inches=0)
fig.savefig('/var/www/speedstat/html/yesterday.png', dpi=100, bbox_inches='tight', pad_inches=0)

fig = plt.figure(figsize=(16, 6))
ax = fig.add_subplot(111)
ax.plot(today['TimeFloat'], today['Download'], 'deeppink', label='Download')
ax.plot(today['TimeFloat'], today['Upload'], 'purple', label='Upload')
ax.plot(today['TimeFloat'], today['Wifi'], 'royalblue', label='Wifi')
ax.set_xticks(timeline)
ax.set_yticks(dataline)
ax.set_ylabel('Speed, Mbit')
ax.set_title(str(date_today))
ax.grid(True)
ax.legend(loc='lower left')
plt.savefig('/var/www/speedstat/html/today.png', dpi=100, bbox_inches='tight', pad_inches=0)

###############################################################

import os
cmd = 'sudo chown -R www-data:www-data /var/www/speedstat/html/yesterday.png'
os.system(cmd)
cmd = 'sudo chown -R www-data:www-data /var/www/speedstat/html/today.png'
os.system(cmd)
