# Leftmost Repeating Character
# Efficient 2

CHAR = 256
def leftmost(st) :
    vis = [False] * CHAR
    res = -1
    for i in range(len(st)-1,-1,-1) :
        if vis[ord(st[i])]==True :
            res = i
        else :
            vis[ord(st[i])] = True
    
    return res
        
st = "abccbd"
print(leftmost(st))