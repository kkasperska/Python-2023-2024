#!/usr/bin/env python
# coding=utf-8

def roman2int(string):
    roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    int = 0
    for i in range(0, len(string)):
        if i == 0 or roman[string[i]] <= roman[string[i-1]]:
            int = int + roman[string[i]] 
        else:
            int = int + roman[string[i]] - 2 * roman[string[i-1]]
            
    return int    
print(roman2int("MCMLXXXVI"))
print(roman2int("XXI"))
print(roman2int("MMXXIII"))
print(roman2int("X"))

#Inny sposób stworzenia słownika:
#roman = {}
#roman["I"] = 1
#roman["V"] = 5
#roman["X"] = 10
#roman["L"] = 50
#roman["C"] = 100
#roman["D"] = 500
#roman["M"] = 1000
