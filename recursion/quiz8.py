def f(n):
    if n==0:
        return
    print (n%2)

    f(n//2)
f(25)