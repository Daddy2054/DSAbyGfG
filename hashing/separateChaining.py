    #Function to insert elements of array in the hashTable avoiding collisions.
def separateChaining( hashSize, arr, sizeOfArray):
        #Your code here
        #return hashtable
        hash_table = [[] for _ in range(hashSize)]
        for i in arr:
            index = i % hashSize
            hash_table[index].append(i)
        return hash_table

print(separateChaining(10, [92,4,14,24,44,91], 6))
print(separateChaining(5, [1, 2, 3, 4, 5, 6], 6))