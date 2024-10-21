def countNonRepeated(arr):
        #Your code here
        res = {arr[0]: 1}
        count = 0
        for i in range(1,len(arr)):
            res[arr[i]]=res.get(arr[i],0)+1  
        for i in res.items():
            if i[1]==1:
                count+=1
        return count



print(countNonRepeated([1, 3, 2, 4, 1, 0, 2, 3 ,0 ,1]))
print(countNonRepeated([9,1,9,1,9,1,0]))
