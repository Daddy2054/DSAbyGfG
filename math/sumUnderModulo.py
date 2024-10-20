#Back-end complete function Template for Python 3

class Solution:
    def sumUnderModulo(self,a,b):
        M = 1000000007
        #sum modulo with M
        return (a%M + b%M) % M
