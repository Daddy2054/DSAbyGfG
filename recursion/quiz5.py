def f(x,y):
    if y ==0:
        return 0
    return(x + f(x, y-1))

print(f(2, 4))