x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
for i in "axby": if ord(i) < 100: print (i)         #Tutaj jest błąd - if powinien być w nowej linii po wcięciu
for i in "axby": print (ord(i) if ord(i) < 100 else i)
