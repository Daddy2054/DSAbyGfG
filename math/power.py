'''
2) Efficient Approach
An optimized Divide and Conquer Solution: The problem can be recursively defined by:

power(x, n) = power(x, n / 2) * power(x, n / 2);        // if n is even

power(x, n) = x * power(x, n / 2) * power(x, n / 2);    // if n is odd
'''
# Function to calculate x raised to the power y in O(logn)

def power(x, y):
    temp = 0
    if  (y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else :
	    return x * temp * temp

print(power(2,3))