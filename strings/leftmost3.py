CHAR = 256 
def leftmost(st) :
    count = [0] * CHAR 
    for i in range(len(st)) :
        count[ord(st[i])] += 1 
    for i in range(len(st)) :
        if count[ord(st[i])] > 1 :
            return i 
    return -1 
    
 
st = "abccbd"  
print(leftmost(st))