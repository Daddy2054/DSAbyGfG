# Leftmost Repeating Character
# Efficient 1 

import sys
CHAR = 256
def leftmost(st) :
    findex = [-1] * CHAR
    res = sys.maxsize
    for i in range(len(st)) :
        if (findex[ord(st[i])]==-1) :
            findex[ord(st[i])] = i
        else :
            res = min(res,findex[ord(st[i])])
    if res == sys.maxsize :
        return -1
    else :
        return res
        
st = "abccbd"
print(leftmost(st))