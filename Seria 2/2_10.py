#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as plik:
    line = plik.read()
    
words = line.split()

print("Liczba wyrazów w napisie: ", len(words))