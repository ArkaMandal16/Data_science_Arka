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