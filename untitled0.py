# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:59:06 2018

@author: v-lazer
"""

import numpy as np
h=np.random.randint(0, 100, (15,10))
h1=h[5:,0:]
print(h, '\\n'*2, h1, '\\n'*2, np.linalg.det(h1))