def printNonRepeated(arr):
    # code here
        mp = {}
        res = []
        for i in range(len(arr)):
            if arr[i] in mp:
                mp[arr[i]] += 1
            else:
                mp[arr[i]] = 1
        for key in mp:
            if mp[key] == 1:
                res.append(key)
        return res

#printNonRepeated([1, 3, 2, 4, 1, 0, 2, 3, 0, 1])
print(printNonRepeated([1, 1, 2, 2, 3 ,3 ,4 ,5 ,6 ,7]))