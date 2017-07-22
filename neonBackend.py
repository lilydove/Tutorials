from neon.backends import gen_backend
from neon.backends.backend import Tensor
import numpy as np

be = gen_backend(backend='cpu')
myTensor = be.zeros((3,3))
print myTensor
#print be.mean(myTensor)
#print be.max(myTensor)

# initialize a numpy array of zeros
array_of_zeros = np.zeros((3,3))

# 1. array of zeros with the shape like the input array
myTensor = be.zeros_like(array_of_zeros)

# 2. initialize a tensor with same values as the input array
myTensor = be.array(array_of_zeros)

# 3. initialize an empty Tensor, then set elements to zero
myTensor = be.empty((3, 3))
myTensor[:] = 9
print be.mean(myTensor)
myNumpyArray = myTensor.get()
np.sqrt(myNumpyArray)
print np.sqrt(myNumpyArray)

# 4. initialize an empty Tensor, then fill the elements to zero
myTensor = be.empty((3, 3))
myTensor.fill(0.0)
print be.mean(myTensor)

# 5. deep copy another Tensor
yourTensor = be.zeros((3, 3))
myTensor = yourTensor.copy(yourTensor)

myNumpyArray = myTensor.get()
print myNumpyArray