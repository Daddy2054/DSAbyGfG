#Prints all divisors but not necessarily in order
def printDivisors1(n):
    i=1 
    while(i*i<=n):
        if(n%i==0):
            print(i)
            if(i!=n/i):
                print(int(n/i))
        i+=1
        
#Prints all divisors in Sorted Order       
def printDivisors2(n):
    i=1 
    while(i*i<n):
        if(n%i==0):
            print(i)
        i+=1 
    
    while(i>=1):
        if(n%i==0):
            print(int(n/i))
        i-=1
            
            
n=15
printDivisors1(n)
printDivisors2(n)