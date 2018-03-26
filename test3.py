# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:18:00 2018

@author: n.cooray
"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are:')
for name in catNames:
    print(' ' + name)