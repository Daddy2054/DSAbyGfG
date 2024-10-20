    #Function to fill the array elements into a hash table 
    #using Quadratic Probing to handle collisions.
def QuadraticProbing(hash, hashSize, arr, N):
    for i in arr:
        index = i % hashSize
        if hash[index] == i:
            continue    
        if hash[index] == -1:
            hash[index] = i
        else:
            j = 1
            while j < hashSize:
                new_index = (index + j * j) % hashSize
                if hash[new_index] == i:
                    break
                if hash[new_index] == -1:
                    hash[new_index] = i
                    break
                j += 1
    return hash
#print(QuadraticProbing([-1] * 11, 11, [21,10,32,43], 4))
#print(QuadraticProbing([-1] * 11, 11, [880,995,647,172], 4))
print(QuadraticProbing([-1] * 11, 11, [3,4,4,4,5,4], 6))