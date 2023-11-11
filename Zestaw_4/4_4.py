def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(1, n):
        a, b = b, a+b
    return b
print(fibonacci(1))
print()  
print(fibonacci(2))
print()
print(fibonacci(10))