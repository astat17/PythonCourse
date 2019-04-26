import numpy as np
import matplotlib.pyplot as plt
p = np.random.poisson(15, 1000)
plt.hist(p)
plt.show()
