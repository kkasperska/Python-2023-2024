#!/usr/bin/env python
# coding=utf-8

with open('line.txt', 'r') as plik:
    line = plik.read()
    
words = line.split()

firstletters = ""

print("Napis stworzony z pierwszych znaków wyrazów:")

for i in range(0, len(words)):
    firstletters = firstletters + words[i][0]

print(firstletters)

lastletters = ""

print("Napis stworzony z ostatnich znaków wyrazów:")

for i in range(0, len(words)):
    lastletters = lastletters + words[i][len(words[i])-1]

print(lastletters)