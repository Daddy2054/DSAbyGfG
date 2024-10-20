#You are given two numbers a and b. Find their GCD using recursion
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
print(GCD(24, 18))  # Output: 6
