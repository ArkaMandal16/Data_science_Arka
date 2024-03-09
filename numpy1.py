import numpy as np

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
