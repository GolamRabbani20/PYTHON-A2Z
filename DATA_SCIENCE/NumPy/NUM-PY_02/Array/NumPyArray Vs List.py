import numpy as np
import time
import sys

#List.................................Memory space......................................................................
s=range(100)
print("Size of an element of a list:",sys.getsizeof(50))

#numpy array.................................Memory space...............................................................
k=np.arange(100)
print("Size of an element of an array:",k[0].size*k.itemsize)

#List.................................Time complexity...................................................................
Size=1000000
L1=range(Size)
L2=range(Size)
start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print("Time in list:",(time.time()-start)*1000)

#NumPy Array.................................Time complexity............................................................
A1=np.arange(Size)
A2=np.arange(Size)
start1=time.time()
Result=A1+A2
print("Time in array:",(time.time()-start1)*1000)
