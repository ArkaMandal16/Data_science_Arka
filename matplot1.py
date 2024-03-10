from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

roll = [1,2,3,4,5]
marks = [10,20,30,40,50]


#plt.scatter(roll ,marks, color = "blue", marker="*")

# plt.figure()

plt.figure(figsize=(5,5))
plt.scatter(roll ,marks, color = "blue", marker="*",)
plt.show()

#plt.plot()
age = [1,2,3,4,6]
weight = [10,20,30,40,50]

plt.plot(age, weight, 'bo',)
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

# Taking iris dataset
