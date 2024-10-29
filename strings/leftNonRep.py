# Leftmost Non-Repeating Element
# Naive

import sys
CHAR = 256
def nonrep(st) :
    fi = [-1] * CHAR 
    for i in range(len(st)) :
        if fi[ord(st[i])] == -1 :
            fi[ord(st[i])] = i
        else :
            fi[ord(st[i])] = -2 
    res = sys.maxsize
    for i in range(CHAR) :
        if fi[i] >= 0 :
            res = min(res,fi[i])
    if res == sys.maxsize :
        return -1
    else :
        return res 
    
    
st = "apple"
print(nonrep(st))