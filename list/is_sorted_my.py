def is_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            for j in range(len(arr)-1):
                if arr[j] < arr[j+1]:
                   return False
            return True
    return True

    # l2 = sorted(l)
    
    # if l==l2:
    #     return True
    # else:
    #     return False

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([5, 4, 3, 2, 1]))