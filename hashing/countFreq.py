def countFreq(arr, n):
    hmp=dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1 
        else:
            hmp[arr[i]]=1 
    for x in hmp:
        print(x, " ", hmp[x])
    
    
n=5
arr=[10, 20, 20, 30, 10]
countFreq(arr, n)