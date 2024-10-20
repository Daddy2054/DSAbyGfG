def smallerThanX(arr,x):
    
    result = []
    for i in arr:
        if i < x:
            result.append(i)
    return len(result)


print(smallerThanX([1, 2, 3, 4, 5, 6,3,2,1, 7, 8, 9, 10], 5))