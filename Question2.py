# Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.
# import numpy as np
# np.random.seed(3)
# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))
# Note: Also add title, xlabel, and ylabel to the plot.

# Solution - 

# Scatter plot is the plot in which the visualization on graph is denoted by dots.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

plt.scatter(x,y)
plt.xlabel("This is X - Axis")
plt.ylabel("This is Y - Axis")
plt.title("This is a Scatter Plot")