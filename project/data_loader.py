#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:31:53 2023

@author: pavel
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('FT1000.csv', delimiter=',', dtype='U20')

country = set(data[:,4])
country.remove('Country')
country = dict(sorted([[str(i),0] for i in country]))

sectors = set(data[:,5])
sectors.remove('Sector')
sectors = dict(sorted([[str(i),0] for i in sectors]))

date = set(data[:,11])
date.remove('FoundingYear')
date = dict(sorted([[str(i),0] for i in date]))

for i in range(1,len(data)):
   country[str(data[i][4])]+=int(data[i][7])
   sectors[str(data[i][5])]+=int(data[i][7])
   date[str(data[i][11])]+=int(data[i][7])
   
# plot for countries    
plt.plot(country.keys(), country.values())

# plot for sectors    
plt.plot(sectors.keys(), sectors.values())

# plot for date    
plt.plot(date.keys(), date.values())
