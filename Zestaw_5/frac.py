import math

def add_frac(frac1, frac2):        # frac1 + frac2
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def sub_frac(frac1, frac2):        # frac1 - frac2
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def mul_frac(frac1, frac2):        # frac1 * frac2
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[0]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def div_frac(frac1, frac2):        # frac1 / frac2
    if (frac1[1] == 0 or frac2[1] == 0 or frac2[0] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1]
    out[1] = frac1[1] * frac2[0]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def is_positive(frac):             # bool, czy dodatni
    if frac[1] == 0:
        raise ZeroDivisionError()
    return True if frac[0] * frac[1] > 0 else False

def is_zero(frac):                 # bool, typu [0, x]
    if frac[1] == 0:
        raise ZeroDivisionError()
    return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError()
    cmp1 = frac1[0] * frac2[1]
    cmp2 = frac2[0] * frac1[1]
    if cmp1 == cmp2:
        return 0
    else:
        return 1 if cmp1 > cmp2 else -1

def frac2float(frac):              # konwersja do float
    return float(frac[0] / frac[1])
