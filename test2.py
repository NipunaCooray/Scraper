# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:10:17 2018

@author: n.cooray
"""

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))