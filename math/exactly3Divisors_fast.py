#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def exactly3Divisors(self,N):
        # code here
        N = int(math.sqrt(N))
        #Initializing counter to zero
        counter=0 
        #Running a loop from 1 to sqrt(N)
        for i in range(1,N+1): 
        
            # A number N only has 3 divisors if it is a  
            # perfect square and its square  root is a prime number, 
            # and we know the number of perfect squares less than N which 
            # is sqrt(N), so just checking if i is prime or not
            if(self.isPrime(i)): 
                counter+=1
        return counter        
    # function to check if N is prime
    def isPrime(self,N):
        if (N==1):
            return False
        for i in range(2,1+int(math.sqrt(N))):
            if N%i==0:
                return False
        return True

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
# } Driver Code Endsf