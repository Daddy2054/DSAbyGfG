# Function to fill the array elements into a hash table
# using Linear Probing to handle collisions.
def linearProbing(hashSize, arr, sizeOfArray):
    # Your code here
    hash_table = [-1] * hashSize
    for i in arr:
        index = i % hashSize    
        if hash_table[index] == i:
            continue        
        if hash_table[index] == -1:
            hash_table[index] = i
        else:
            j = 1
            while j < hashSize:
                new_index = (index + j) % hashSize
                if hash_table[new_index] == i:
                    break
                if hash_table[new_index] == -1:
                    hash_table[new_index] = i
                    break
                j += 1
    return hash_table


#print(linearProbing(4, [4, 14, 24, 24, 44], 5))
print(linearProbing(8, [0, 12, 8, 3, 3, 21 ,13, 13 ,5, 7, 16], 11))
#0 8 7 3 12 21 13 5
