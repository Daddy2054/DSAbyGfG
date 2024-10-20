#User function Template for python3

def digitsInFactorial(N):
        # code here
        x = 1
        for i in range(2, N + 1):
            x *= i

        res = 0

        while x>0:
    
            x=x//10
            res = res + 1
        return res


print(digitsInFactorial(120))
