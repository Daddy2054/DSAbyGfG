
def func(x,y):
    if x == 0:
        return y
    else:
        return func(x-1,x+y)
    
print(func(4, 3))