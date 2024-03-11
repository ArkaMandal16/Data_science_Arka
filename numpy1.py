import numpy as np
import matplotlib.pyplot as plt
#Declaration of numpy arrays

a = np.array([1,2,3])
print("1D array")
print(a)

b = np.array([[1,2,3],
             [1,2,3]])
print("2D array")
print(b)

c = np.array([[1,2,3],
             [1,2,3],
             [1,2,3]])
print("3D array")
print(c)

# type

print(type(a))
print(type(b))
print(type(c))

#size of array

print(a.size)
print(b.size)
print(c.size)

# shape of array

print(a.shape)
print(b.shape)
print(c.shape)

#datatype of arrays

print(a.dtype)
print(b.dtype)
print(c.dtype)

# transpose of array

print(a.transpose())
print(b.transpose())
print(c.transpose())

# empty function : creates empty array of random data: print(np.empty((row,col), dtype = blahblah))

print(np.empty((1,2), dtype = int))

# ones function: np.ones((row,col), dtype = blahvlah):prints only one element in places = 1
# default data type is float
x = np.ones((3,3))
print(x)

y= np.ones((3,4), dtype = int)
print(y)

#zeros function

y= np.zeros((3,4), dtype = bool)
print(y)

#arange function: np.arange(start,end,step): works kinda like a for loop

print(np.arange(1,10,2))

# reshape function: arr.reshape((row,col))

print(b.reshape(3,2))

# flatten function : inverse of reshape
# it returns copy of original array. if anyvalues are modified in this array, the original array is not affected.

print(b.flatten())

#ravel function : same work as flatten but different functionality. if anyvalues are modified in this array, the original array is affected.

print(b.ravel())

# numpy array slicing

arr = np.arange(1,21)
arr = arr.reshape(5,4)
print(arr)

print(arr[1])
#output = [5 6 7 8]
print(arr[2,3])
#output = 12
print(arr[1:3])
#output = [[ 5  6  7  8]
#           [ 9 10 11 12]]
print(arr[:2])
#output = [[1 2 3 4]
#         [5 6 7 8]]
print(arr[:,2])
#OUTPUT = [ 3  7 11 15 19]
print(arr[1:3 , 2])
#output= [ 7 11]

# numpy math

ar = np.arange(1,11).reshape(2,5)
br = np.arange(21,31).reshape(2,5)

print(ar)
print(br)

# numpy array sum
print(np.add(ar,br))

#numpy array subtract
print(np.subtract(ar,br))

#numpy array multiply (only elements in consecutive places)
print(np.multiply(ar,br))

#numpy array division (only elements in consecutive places)
print(np.divide(ar,br))

#numpy matrix multiplication

# 1. first check ar[col]=br[row]. if not, reshape br.
br = br.reshape(5,2)
mul = np.dot(ar,br)
print(mul)

#some othe functions
print(mul.max())
print(mul.min())
print(mul.argmax())
print(mul.argmin())
print(np.sum(mul, axis=1))
print(np.sum(mul, axis=0))

#numpy trig functions

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

# random function 

r = np.random.random(5)
print(r)

d = np.random.random((2,2))
print(d)

sex = np.random.random((3,2,2))
print(sex)

ohh = np.arange(1,10)
print(np.random.choice(ohh))

#string operations 

s1 = "hi ishika"
s2 = "i love you"

print(np.char.add(s1 ,s2))
print(np.char.upper(s1))
print(np.char.lower(s1))

print(np.char.split(s1))
print(np.char.splitlines(s2))
print(np.char.replace(s1, 'hi', 'hello'))
print(np.char.center('hi', 6, '*'))
