# imported numpy
import numpy as np
# Printing a random 10*10
x=np.random.random((10, 10))
print(x)
# Printing max values in all the rows
print("Max values in each row are",x.max(1))
# Printing min values in all the rows
print("Min values in each row are",x.min(1))