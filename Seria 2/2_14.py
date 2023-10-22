#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as plik:
    line = plik.read()
    
words = line.split()
longestword = ""
maxlength = 0

for i in range(0, len(words)):
    if len(words[i]) > maxlength:
        longestword = words[i]
        maxlength = len(words[i])
        
print("Najdłuższe słowo w napisie to:", longestword)
print("Długość słowa:", maxlength)
        