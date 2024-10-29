def leftmost(st) :
    for i in range(len(st)) :
        for j in range(i+1 , len(st)) :
            if st[i] == st[j] :
                return i 
            
    return -1 
    
st = "cabba"
print(leftmost(st))
