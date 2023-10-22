#!/usr/bin/env python
# coding=utf-8

L = [67, 12, 7, 66, 650, 141, 5, 56, 48, 9, 0, 123]
Ls = [str(i) for i in L]

for i in range(0, len(Ls)):
    Ls[i] = Ls[i].zfill(3)
    
print(Ls)