import cmath
import cmd
from itertools import filterfalse
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
  
#import pandas as pd
import scipy.integrate 
import scipy.integrate as integrate
import scipy.special as special
from scipy import signal
####################################

f = open("test_data.txt", "r")
lines = f.readlines()
f.close()

lines = str(lines)
text = lines.split(" ")

A = []
x = []
y = []
z = []

nr = []
for data in text:
    nr.append(data)
 
for i in range(1, len(nr)-7, 8):
    A.append(int(nr[i].split("' ")[0]))
    x.append(int(nr[i + 2].split("' ")[0]))
    y.append(int(nr[i + 4].split("' ")[0]))
    z.append(int(nr[i + 6].split("' ")[0]))

for i in range(100):
    print(f"=>{A[i]}, =>{x[i]}, =>{y[i]}, =>{z[i]}")

####################################

# x = [ i * 10 for i in x ]

# y = [ i * 10 for i in y ]

# z = [ i * 10 for i in z ]


x = signal.detrend(x)
y = signal.detrend(y)
z = signal.detrend(z)


# creating a dummy dataset


timeStep = 0.017  # time step of ground motion data

N = len(x)
time = np.linspace(0.0, N*timeStep, N) # duration vector 
dt = mean(diff(time))
fs = 1/dt;  # frequency

# some additionnal high pass filtering
N = 2
fc = 0.5; #Hz
[B,C] = signal.butter(N,2*fc/fs,'high')

x = signal.lfilter(B, C, x)
y = signal.lfilter(B, C, y)
z = signal.lfilter(B, C, z)

x_velocity = scipy.integrate.cumtrapz(x, dx = dt, initial = 0) #acceleration to velocity
y_velocity = scipy.integrate.cumtrapz(y, dx = dt, initial = 0)
z_velocity = scipy.integrate.cumtrapz(z, dx = dt, initial = 0)  


x_velocity = detrend(x_velocity)
y_velocity = detrend(y_velocity)
z_velocity = detrend(z_velocity)


x_displacement = scipy.integrate.cumtrapz(x_velocity, dx = dt)
y_displacement = scipy.integrate.cumtrapz(y_velocity, dx = dt)
z_displacement = scipy.integrate.cumtrapz(z_velocity, dx = dt)



fig = plt.figure(figsize=(12,12))

ax = fig.add_subplot(111,projection='3d')
n = 100


colmap = cm.ScalarMappable(cmap=cm.hsv)
A.pop()

A =[abs(i) for i in A]

colmap.set_array(A)

A = [i/max(A) for i in A]
print(A) 



yg = ax.scatter(x_displacement, y_displacement, z_displacement, c=cm.hsv(A), marker='o')
cb = fig.colorbar(colmap)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()




# https://onelinerhub.com/python-matplotlib/how-to-plot-3d-heatmap
# https://makersportal.com/blog/2017/9/25/accelerometer-on-an-elevator
# https://koalatea.io/python-detrending-time-series/
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.integrate.cumtrapz.html