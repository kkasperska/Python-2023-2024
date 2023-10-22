#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as plik:
    line = plik.read()
    
words = line.split()

lengths = []
for i in range(0, len(words)):
    lengths.append(len(words[i]))
    
print("Łączna długość wyrazów w napisie: ", sum(lengths))