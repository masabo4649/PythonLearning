# http://at.hatenadiary.com/entry/2017/07/02/001500

print ("Hello World")

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 15, 1000)
print (x)
plt.plot(x, np.sin(x))
