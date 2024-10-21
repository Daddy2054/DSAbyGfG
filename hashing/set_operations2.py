s1 = {2, 4, 6, 8}
s2 = {4, 8}

print('disjoint sets:', s1.isdisjoint(s2))

print('isSubset:', s1 <= s2)
print(s1.issubset(s2))

print('proper set:', s1 < s2)

print('s1 is superset of s2:', s1 >= s2)
print(s1.issuperset(s2))

print('s1 is proper superset of s2:', s1 > s2)
