#!/usr/bin/env python
# coding=utf-8

while True:
    x = input("Podaj liczbę rzeczywistą ")
    if x == "stop": break
    try: n = float(x)
    except:
        print("Błąd - to nie jest liczba")
        continue
    print("Liczba: ", x, " Trzecia ptęga liczby: ", pow(n,3))