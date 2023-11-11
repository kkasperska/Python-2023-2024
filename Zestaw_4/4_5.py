def odwracanieit(L,left,right):
    stop = (right-left)//2
    for i in range(stop+1):
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1
    return L

def odwracanierek(L, left, right):
    if (right - left) <= 0:
        return L
    else:
        L[left], L[right] = L[right], L[left]
        return odwracanierek(L, left+1, right-1)
    
L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = [1,2,3,4,5,6,7,8,9,10]

print(L1)
print()
print(odwracanieit(L1,2,6))
print()
print(L2)
print()
print(odwracanierek(L2,2,6))