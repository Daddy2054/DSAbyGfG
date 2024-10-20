def reverseList(l):
    s = 0
    e = len(l) - 1

    while s < e:
        l[s], l[e] = l[e], l[s] # swapping left element to right and right element to left
        s = s + 1
        e = e - 1

# l = [10,20,30]
# l.reverse()     # reverse given list
# print(l)

# l = [10,20,30]
# new_l = list(reversed(l))   # return new reversed list
# print(new_l)

# l = [10,20,30]
# new_l = l[::-1]             # return new reversed list
# print(new_l)







l = [int(x) for x in input().split(',')]
reverseList(l)
print(l)

