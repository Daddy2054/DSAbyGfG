#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        #output=""
        #n=1
        def print1toN(N,n):
            if N == 0:
                return
            if n == N+1:
                return
            print(n,end=" ") 
            print1toN(N,n+1)

        print1toN(N,1)
        #print(output)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends