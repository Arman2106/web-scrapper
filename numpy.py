#numpy basics
import numpy as np

#creating an array
a = np.array([1,2,3])
print(a) #[1 2 3]

#numpy methods
#array
#zeros
#ones
#empty
#arange
#linspace
#random.rand
#random.randn
#random.randint
#reshape
#ravel
#min
#max
#argmin
#argmax
#shape
#dtype


print()

#creating a 2D array
b = np.array([[1,2,3],[4,5,6]])
print(b)
#[[1 2 3]
# [4 5 6]]

print()

#creating a 3D array
c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c)
#[[[ 1  2  3]
#  [ 4  5  6]]   
# [[ 7  8  9]
#  [10 11 12]]]

print()

#creating an array with a specified datatype
d = np.array([1,2,3], dtype=complex)
print(d) #[1.+0.j 2.+0.j 3.+0.j]

print()

#creating an array with zeros
e = np.zeros((3,3))
print(e)

#[[0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]]
print()


#creating an array with ones
f = np.ones((3,3))
print(f)

#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
print()

