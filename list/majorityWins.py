    #Function to find element with more appearances between two elements in an array.    
def majorityWins(arr, x, y):
        # code here
    count_x = arr.count(x)
    count_y = arr.count(y)
    if count_x > count_y:
        return x
        
    elif count_y > count_x:
        return y
    #If both elements have the same frequency, then return the smaller element.
    else:
        return min(x, y)
    
print(majorityWins([1,1,2,2,2,2,2,3,3,4,4,4,4,4], 4, 2))
print(majorityWins([], 4, 3))