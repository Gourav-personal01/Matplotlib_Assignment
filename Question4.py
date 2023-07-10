# Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
# import numpy as np
# company = np.array(["Apple", "Microsoft", "Google", "AMD"])
# profit = np.array([3000, 8000, 1000, 10000])

# Solution ---
# Bar plot represents the graph between numeric values and the string values. it is used to visualize the details like growth data,person vs year data etc.
import numpy as np
import matplotlib.pyplot as plt
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

plt.bar(company,profit)
plt.show()