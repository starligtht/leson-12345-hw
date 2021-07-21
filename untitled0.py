# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 21:01:14 2021

@author: 88697
"""

score = int(input('enter grade 0-100 '))


if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print ('C')
elif score >= 60:
    print('D')
elif score == 0:
    print('what are you doing in class?')
else:
    print ('E')