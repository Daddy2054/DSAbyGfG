def getByIndex(arr,n,idx):
    if n<=idx+1:
        return  -1
    return arr[idx]


l= [1,2,3,4,5]
l2 =l.reverse()
print(getByIndex(l,5,3332))

print(l)