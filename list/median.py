
import math
def median(A,N):
        A.sort()
        middle = N // 2
        med = A[middle]
        if N % 2 == 0:
            med = (A[middle - 1] + A[middle]) / 2
            med = math.floor(med)
        return med
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
def mean(A,N):
        ##Your code here
    return math.floor(sum(A) / N)


a = [1, 2, 19, 28, 5]
print(mean(a,5),median(a,5))
