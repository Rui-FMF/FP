def primesUpTo(n):
    lst = [x for x in range(2, n+1) for y in range(2,x) if (x%y!=0)]
    return lst
    
print(primesUpTo(120))
