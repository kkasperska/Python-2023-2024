import itertools
import random


def a():
    itera = itertools.cycle([0,1])

    for i in range(20):
        print(next(itera), end = ", ")

def b():
    iterb = iter(lambda: random.choice(["N","E","S","W"]), 1)

    for i in range(20):
        print(next(iterb), end = ", ")


def c():
    iterc = itertools.cycle([0,1,2,3,4,5,6])

    for i in range(20):
        print(next(iterc), end = ", ")


if __name__ == "__main__":
    a()
    print()
    b()
    print()
    c()
    print()