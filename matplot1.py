from turtle import color
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

roll = np.arange(1,6)
marks = np.arange(10,60,10)


#plt.scatter(roll ,marks, color = "blue", marker="*")

# plt.figure()

plt.figure(figsize=(5,5))
plt.scatter(roll ,marks, color = "blue", marker="*",)
plt.show()

#plt.plot()
age = [1,2,3,4,6]
weight = [10,20,30,40,50]

plt.plot(age, weight, 'r--')
plt.show()

#plotting multiple data on same graph
temp_kol = [25,26,27,26,25]
humid_kol = [55,56,25,50,45]

temp_kal = [35,28,29,16,26]
humid_kal = [55,66,25,30,45]

plt.figure(figsize=(8,8))
plt.xticks(np.arange(0,70,10))
plt.yticks(np.arange(10,40,5))

plt.xlabel('humidity')
plt.ylabel('temperature')

plt.scatter(temp_kal, humid_kal, color='blue',)
plt.scatter(temp_kol, humid_kol, color='red')

plt.show()

#subplot function 
print(np.pi)
print(np.sin(np.pi/6))

x_sin = np.arange(0,10*np.pi,0.1)
y_sin = np.sin(x_sin)

plt.plot(x_sin,y_sin)
plt.show()

x_cos = np.arange(0,10*np.pi,0.1)
y_cos = np.cos(x_cos)

plt.plot(x_cos,y_cos)
plt.show()

plt.subplot(2,1,1)
plt.plot(x_sin,y_sin)
plt.title("sin curve")

plt.subplot(2,1,2)
plt.plot(x_cos,y_cos)
plt.title("cos curve")

plt.show()

# Taking iris dataset
