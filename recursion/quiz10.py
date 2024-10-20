def f(n):
    if n>0:
        return (n+f(n-2))
    else:
        return 0 
print(f(10))