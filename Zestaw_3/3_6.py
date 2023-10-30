#!/usr/bin/env python
# coding=utf-8

szerokosc = int(input("Podaj dszerokość prostokąta "))
wysokosc = int(input("Podaj wysokość prostokąta "))
prostokat = ""

for k in range(0, wysokosc):
    for i in range(0, szerokosc):
        prostokat = prostokat + "+---"
        
    prostokat = prostokat + "+\n"

    for i in range(0, szerokosc):
        prostokat = prostokat + "|   "
        
    prostokat = prostokat + "|\n"
    
for j in range(0, szerokosc):
        prostokat = prostokat + "+---" 

prostokat = prostokat + "+"


print(prostokat)