# Complete the function isPalin that takes n as parameter and returns true or false , using recursive call
def isPalin(n):
    # converting the integer to string
    n = str(n)

    # base case
    if len(n) == 0 or len(n) == 1:
        return True

    # checking first and last characters
    if n[0] == n[-1]:
        # recursively calling function with sliced string
        return isPalin(n[1:-1])
    else:
        return False
    
print(isPalin(1231))  # True

