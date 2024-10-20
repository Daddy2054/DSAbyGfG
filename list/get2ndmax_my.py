def getMax(l):
    if not l:
        return None
    else:

        res = l[0]                  # assume l[0] is the max
        res2 = l[1]                  # assume l[1] is the 2nd max
        for i in range(2, len(l)):  # iterate through index 1 to last
            if l[i] > res:  
                res2 = res         # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
            elif l[i] > res2 and l[i] != res:       # check whether current element is greater than res2
                res2 = l[i]     
#            print(res, res2)    # if current element is greater than res2 ,update res2 to current
    if res == res2:
        return None
    return res2  

# O(n)

l = [20,10,20,30,8,12]
print(getMax(l))
l = [10,10,10]
print(getMax(l))