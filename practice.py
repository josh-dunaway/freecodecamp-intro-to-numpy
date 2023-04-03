import sys
import numpy as np

# In Python, everything is an object, even 'integers' = 'boxed ints'
VALUE = 4
# lots of 'stuff' comes with simple integer in python
print(dir(VALUE))

# NumPy uses primitive numeric types, making storing and comp. efficient
a = np.array([1, 2, 3, 4])
b = np.array([0, .5, 1, 1.5, 2])

# setting data type of filling array
N = 100
c = np.zeros(N, dtype=np.int8)
for i in range(1, N):
    c[i] = i

d = np.array(['a', 'b', 'c'])

# print array types for above arrays
print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d.dtype)

# can dictate custom ranges in print calls
print(c[0:20])
print(c[::20])
print(d)

# dimensions and shapes