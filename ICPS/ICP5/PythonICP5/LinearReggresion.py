import numpy as np
import matplotlib . pyplot as plt
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
x_ = np.mean(x)
y_ = np.mean(y)
B1 = np.sum((x-x_)*(y-y_))/np.sum(np.power(x-x_, 2))
B0 = y_ - (B1*x_)
print(B1)
print(B0)
y1 = B0 + (B1*x)
plt.scatter(x,y,y1, color='red')
plt.plot(x,y,y1)
plt.show()

