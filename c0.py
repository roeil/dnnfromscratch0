import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


nr = np.random.normal(0,10,500)
xs = np.sin(nr)
ys = np.cos(nr)
plt.scatter((xs),(ys))
