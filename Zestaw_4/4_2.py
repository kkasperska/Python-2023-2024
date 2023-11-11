def make_ruler(n):
    ruler = n*"|...."+"|\n"
    num = ""

    for i in range(0, n):
        num = num + str(i) + (" " * (5 - len(str(i))))
        
    num = num + str(n)
    
    ruler = ruler+num
    
    return ruler

def make_grid(x,y):
    
    line1 = x*"+---"+"+\n"
    line2 = x*"|   "+"|\n"

    grid = y*(line1+line2)+line1

    return grid

print(make_ruler(12))
print()
print(make_grid(5,3))