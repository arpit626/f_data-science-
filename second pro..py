#WRITE A NUMPY PROGRAM TO TEST WHETHER NONE OF THE ELEMENTS OF A GIVEN ARRAY ARE ZERO
import numpy as np
x =np.array([1,2,3,4,5])
print("original array: \n",x)
print ("test if none of the elements of the array is zero: \n",np.all(x))
import numpy as np
x =np.array([0,2,3,4,5])
print("original array: \n",x)
print("test if none of the elements of the said aray is zero:\n",np.all(x))

