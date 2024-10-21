s1 = {2, 4, 6, 8}

s2 = {3, 6, 9}

print('union ', s1 | s2)
print(s1.union(s2))

print('intersecton', s1 & s2)
print(s1.intersection(s2))

print('present in s1, but not present in s2', s1 - s2)
print(s1.difference(s2))

print('symmetric differences, not present in both', s1 ^ s2)
