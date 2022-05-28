# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:21:06 2022

@author: Ace
"""

import matplotlib.pyplot as plt
data = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]

        
        
        ]


plt.imshow(data, cmap="gray")
plt.show()