# Importing Libraries
from matplotlib import pyplot as plt
import numpy as np
import time

# Open file, it is in the same folder where program file is kept.
file = open("subscription.csv", 'r')
title = file.readline()

'''
The "subscription.csv" file conataining data readed from IoT connected to device
in office and AWS IoT cloud.

Data file is not actually in comma separated value, just assume that data is
present in any formate. We are going to read these values and plot these values
using matplotlib library.

Comma Separated title names:-
format,payload,qos,timestamp,topic

Filled values are:-
string,Humidity:45.000000  Temperature:24.000000'C,0,1560500284447,mqtt
'''

titles = title.split(',')
read = file.readline()

# string,Humidity:45.000000  Temperature:24.000000'C,0,1560500284447,mqtt
humidity = []
temperature = []
timeval = []

while read:
    all_data = read.split(',')
    data = all_data[1]  # Humidity:45.000000  Temperature:24.000000'C
    timestamp = int(all_data[3])//1000

    #timeval.append(time.strftime("%D %H:%M:%S", time.localtime(timestamp)))
    timeval.append(time.strftime("%M:%S", time.localtime(timestamp)))

    # Data retrieving 
    data = data.split('  ')
    # data => [Humidity:45.000000, Temperature:24.000000'C]

    humidity.append(int((data[0].split(':'))[1].split('.')[0]))
    
    temp = data[1].split(':')[1].split("'")
    temperature.append(int(temp[0].split('.')[0]))
    read = file.readline()

x = len(humidity)
x = np.arange(x)
plt.xlabel("Time")
plt.ylabel("Sensor Data")

plt.plot(timeval[80:], humidity[80:], marker='o', markerfacecolor='blue', color="skyblue")
plt.plot(timeval[80:], temperature[80:], color="red")
plt.legend(['% Humidity', 'Temperature in *C'], loc='upper left')
plt.show()
