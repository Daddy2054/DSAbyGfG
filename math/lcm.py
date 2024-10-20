# GCD and HCF of two numbers
# Efficient
# https://ide.geeksforgeeks.org/790653a6-a3b4-4906-89ef-03ad5e5c28bf

def gcd(a,b):
    
    if b == 0 :
        return a
    return gcd(b, a % b)
    
def lcm(a,b) :
    return a * b // gcd(a,b)

a = 12
b = 15
print(lcm(a,b))