#!/usr/bin/env python
# coding=utf-8

L = [[],[4],(1,2),[3,4],(5,6,7)]
L2 = []

for i in range (0, len(L)):
    suma = 0
    for j in range(0, len(L[i])):
        suma = suma + L[i][j]
    
    L2.append(suma)
    
print(L)
print(L2)