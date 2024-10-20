# Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.

# The Best Solution is to do bitwise XOR of all the elements. XOR of all elements gives us odd occurring elements. 

def findodd(arr) :
    
    res = 0 
    
    for i in arr :
        res = res ^ i 
        
    return res
    
    
#if __name__ == "__main__" :
arr = [4,3,4,4,4,5,5,3,3]
print(findodd(arr))
