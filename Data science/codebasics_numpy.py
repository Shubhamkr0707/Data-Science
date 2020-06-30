import numpy as np 
# a=np.array([5,6,9], dtype=float)
# print(a)
# b=np.zeros((2,2))
# print(b)
# c=np.arange(1,5)
# print(c)
x=[[11,12,13],[21,22,23],[31,32,33]]
y=np.array(x)
print(y)
print(y.shape)
print(y.reshape(9,1))
# For one dimension
print(y.ravel())
# for min value
m=y.min()
print(m)
print(y.max())
print(y.sum())
print(y.sum(axis=1))
print(np.sqrt(y))