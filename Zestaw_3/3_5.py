#!/usr/bin/env python
# coding=utf-8

dlugosc = int(input("Podaj długość linijki "))
linijka = ""
for i in range(0, dlugosc):
    linijka = linijka + "|...."
    
linijka = linijka + "|\n"

for i in range(0, dlugosc):
    linijka = linijka + str(i) + (" " * (5 - len(str(i))))
    
linijka = linijka + str(dlugosc)
print(linijka)