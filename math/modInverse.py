#Back-end complete function Template for Python 3
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
class Solution:
    def modInverse(self,a,m):
        
        # taking mod of a with m
        a=a%m
        
        # For every number x, check if (a*x)%m is 1
        for x in range(1,m):
            if((a*x)%m==1):
                return x
        
        return -1

'''
Expected Approach:
Intuition:
A number x is said to modular multiplicative inverse of a under m if (a%m * x%m)%m = 1. Since x%m lies in between 0 to m-1 and we need to find the smallest x. Thus we will simply iterate over all possible values of x%m i.e from 0 to m-1 and will check if the condition holds true.

Implementation:
Step 1- Run a for loop from 0 to m-1.
Step 2- For each value of x find the value of the expression (a%m *x)%m and if it is 1 then return x.
Step 3- Return -1.
'''