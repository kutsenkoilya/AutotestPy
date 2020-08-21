# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:46:50 2020

@author: kompich
"""

import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))