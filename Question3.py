# Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# Use the following data:
# import numpy as np
# For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])


# Solution ---
# subplot( m , n , p ) divides the current figure into an m -by- n grid and creates axes in the position specified by p


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 100, 200, 300, 400, 500])

plt.subplot(2,2,1)
plt.plot(x,y)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([50, 20, 40, 20, 60, 70])
plt.subplot(2,2,1)
plt.plot(x,y)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(2,2,1)
plt.plot(x,y)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(2,2,1)
plt.plot(x,y)
plt.show()
