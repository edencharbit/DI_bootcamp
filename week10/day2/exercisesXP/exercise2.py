# Exercise 2 : Type Conversion and Array Operations

import numpy as np

lst_float = [3.14, 2.17, 0, 1, 2]
array_float = np.array(lst_float)
array_int = array_float.astype(int)
print(array_int)
