import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5])
print("1-dimensional array:", a)

# Create a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2-dimensional array:")
print(b)

# Get the shape of an array
print("Shape of array b:", b.shape)

# Reshape an array
c = b.reshape((3, 2))
print("Reshaped array:")
print(c)

# Transpose an array
d = c.T
print("Transposed array:")
print(d)

# Get the minimum and maximum values of an array
print("Minimum value of array d:", d.min())
print("Maximum value of array d:", d.max())

# Get the mean and standard deviation of an array
print("Mean of array d:", d.mean())
print("Standard deviation of array d:", d.std())

# Access elements of an array using indexing
print("Element at index (0,1) of array d:", d[0,1])

# Access sub-arrays using slicing
print("First row of array d:", d[0,:])

# Add two arrays
e = np.array([1, 2, 3])
f = np.array([4, 5, 6])
g = e + f
print("Sum of arrays e and f:", g)

# Multiply an array by a scalar
h = 2 * e
print("Array e multiplied by 2:", h)

# Dot product of two arrays
i = np.dot(e, f)
print("Dot product of arrays e and f:", i)

# Use a boolean mask to filter elements of an array
mask = e > 2
print("Boolean mask:", mask)
print("Elements of e greater than 2:", e[mask])

# Use the linspace function to create an array of evenly spaced values
j = np.linspace(0, 10, 5)
print("Array of evenly spaced values:", j)
