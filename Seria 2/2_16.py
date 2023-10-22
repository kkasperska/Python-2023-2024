#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as plik:
    line = plik.read()
    
line2 = line.replace("GvR", "Guido van Rossum")
print(line2)
