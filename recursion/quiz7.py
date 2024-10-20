def f(x):
    if x==0:
        return
    else:
        print("a")
        return f(x-1)
    
f(10)