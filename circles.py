import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

nr0=np.random.uniform(0.7,1.3,500)#. uniform(-10,10,500)
nr1=np.random.uniform(-0.7,1.3,500)#. uniform(-10,10,500)
nr=np.random.normal(0,10,500)#. uniform(-10,10,500)
nr2=np.random.normal(0,10,500)#. uniform(-10,10,500)
xs=np.sin(nr)#*10+np.random.ranf(len(nr))
ys=np.cos(nr)#*10+np.random.ranf(len(nr))

xs0=np.sin(nr0)#*10+np.random.ranf(len(nr))
ys0=np.cos(nr0)#*10+np.random.ranf(len(nr))

plt.scatter((xs*nr0),(ys*nr0))
plt.scatter(0.5*xs*nr1,0.5*ys*nr1)