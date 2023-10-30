#!/usr/bin/env python
# coding=utf-8

sekwencja1 = "abcd12345qwertyabcd"
sekwencja2 = "76321defghtrewq890765"

powtorzone = ""
wszystkie = ""

for i in sekwencja1:
    for j in sekwencja2:
        
        if i == j:
            if not powtorzone.__contains__(i):
                powtorzone = powtorzone + i

znaki = sekwencja1 + sekwencja2
for i in znaki:
    if not wszystkie.__contains__(i):
        wszystkie = wszystkie + i
        
print("Sekwencja 1: ", sekwencja1)
print("Sekwencja 2: ", sekwencja2)
print("Powtórzone znaki: ", powtorzone)
print("Wszystkie znaki: ", wszystkie)