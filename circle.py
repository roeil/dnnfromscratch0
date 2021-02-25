#cicrle
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

nr=np.random.normal(0,10,500)#. uniform(-10,10,500)
xs=np.sin(nr)#*10+np.random.ranf(len(nr))
ys=np.cos(nr)#*10+np.random.ranf(len(nr))
plt.scatter(xs,ys)