"""
计算球体的表面积
"""

import math
from re import L

def surface(r):
    s = 4*math.pi*r**2
    return s

lis = [1, 2, 4, 9, 10, 13]
for i in lis:
    print("%.2f"%surface(i))