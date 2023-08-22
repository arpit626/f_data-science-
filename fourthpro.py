#WRITE A NUMPY PRO.TO CREATE AN ARRAY WITH THE VALUES OF 1,7,105 AND DETERMINE THE SIZE OF MEMEORY OCCUIPIED BY THE ARRAY 
import numpy as np
X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))

