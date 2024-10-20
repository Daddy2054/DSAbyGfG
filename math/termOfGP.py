#Back-end complete function Template for Python 3

class Solution:
    def termOfGP(self,A,B,N):
        # common ratio is given by r=b/a
        r=B/A 
        # Nth term is given by a(r^(N-1))
        return A*pow(r,N-1) 
