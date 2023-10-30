L = [3, 5, 4] ; L = L.sort()        #Sort nie zwraca żadnej wartości, wystarczy L.sort() bez przypisania
x, y = 1, 2, 3             #Za dużo wartości do przypisania
X = 1, 2, 3 ; X[1] = 4        #Nie można zmieniać wartości w tuple
X = [1, 2, 3] ; X[3] = 4        #W liście nie ma elementu o indeksie 3
X = "abc" ; X.append("d")       #String nie ma metody append
L = list(map(pow, range(8)))        #Brak argumentów w pow