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
	fX = open('irisX.txt','r')
	fy = open('irisY.txt','r')
	a = np.array([(1,2,3,3), (3,4,4,4)])
	a = np.append(a, [(6,6,6,3)], axis = 0)
	for line in fX:
		b = np.fromstring(line,sep=',')
		print b
		a = np.append(a, [(b)], axis = 0)
	X = a
	y = np.array([0,0,0])
	for line in fy:
		y=np.append(y, float(line))
	return X,y

X,y = getData()
classes = np.unique(y) # Get the unique examples
print classes

# Iterate over both index and value
for jdx, lclass in enumerate(classes):
	idx = y==lclass # Returns a true or flase with the length of y
	idx = np.where(y==lclass)[0]
	xlc = X[idx,:] # Get the x for the class labels. Vectors are rows.

# Subtract the vector using a for loop
X = np.array([(1,2,3),(4,5,6),(7,8,9)])
print X
u = np.array((1,2,3))

for i_row in range(0, X.shape[0]):
	X[i_row,:] = X[i_row,:] - u
print(X)

# Subtract using broadcasting
X = np.array([(1,2,3),(4,5,6),(7,8,9)])
u = np.array((1,2,3))
X = X - u
print X
