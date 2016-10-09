import numpy as np

# Dimensions of Matrices
rows = 7
cols = 4
depth = 5

# Creating matrices
A = np.zeros((rows, cols)) # 2D Matrix of zeroes
print (A.shape)
A = np.zeros((depth, rows, cols)) # 3D Matrix of zeroes
A = np.ones((rows, cols)) # 2D Matrix of ones
A = np.array([(1,2,3),(4,5,6),(7,8,9)]) # 2D 3x3 matrix with values

# Turn it into a square diagonal matrix with zeros of-diagonal
d = np.diag(A) # Get diagonal as a row vector
d = np.diag(d) # Turn a row vector into a diagonal matrix
print(d)

# This works
print(1.0/A)

# Numpy reshaping

a = np.array((1,2,3))
print(a.shape)

print(a.reshape(-1,1).shape)

print(a.reshape(1,-1).shape)

print(a.reshape(1,-1).reshape(-1).shape)

def getData():
	print("hello world")
	f = open('irisX.txt','w+')
	for line in f:
		print line
	f.write('test lol\n')

getData()
