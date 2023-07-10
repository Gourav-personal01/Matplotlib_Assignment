# Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
# box1 = np.random.normal(100, 10, 200)
# box2 = np.random.normal(90, 20, 200)

# Solution --

# box on displays the box outline around the current axes by setting its Box property to "on"
import matplotlib.pyplot as plt
import numpy as np

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

plt.plot(box1,box2)
plt.box(on = True)