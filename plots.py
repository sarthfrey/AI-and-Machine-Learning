# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:43:33 2015

@author: Sarth
"""

import numpy as np
import pylab
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100000)
y = x*x
pylab.plot(x,y)


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

