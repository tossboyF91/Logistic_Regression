#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:32:49 2018

@author: pengsu
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100,100,20)
y = 1 / (1 + np.e**(-x))

plt.figure()
plt.plot(x,y)