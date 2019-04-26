import numpy as np
import matplotlib.pyplot as plt
p = np.random.pareto(12, 1000)
plt.hist(p)
plt.show()
