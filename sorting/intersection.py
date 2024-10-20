def intersection(a, b, m, n):
    i=0 
    j=0 
    while(i<m and j<n):
        if(i>0 and a[i-1]==a[i]):
            i=i+1 
            continue
        if(a[i]<b[j]):
            i=i+1 
        elif(b[j]<a[i]):
            j=j+1 
        else:
            print(a[i], end=" ")
            i=i+1 
            j=j+1 
    
    
    
            
a=[10, 20, 35, 40]
b=[20, 35, 50, 90]
intersection(a, b, len(a), len(b))