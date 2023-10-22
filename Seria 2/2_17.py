#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as file:
    line = file.read()
    
words = line.lower().split()

wordsalphabet = sorted(words)
print(wordsalphabet)
print()
wordslength = sorted(words, key=len)
print(wordslength)