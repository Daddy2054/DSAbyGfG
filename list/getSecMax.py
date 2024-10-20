def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]; slar = None

    for x in l[1:]:
        if x > lar:         # if current element is greater than lar(largest element)
            slar = lar          # update slar to largest
            lar = x         # update lar to current element(largest)

        elif x != lar:      # if x is less then largest and not equal to lar(largest element)
            if slar == None or slar < x:    # if x is greater then second largest
                slar = x                    # assign current element is second largest
    return slar
inp=[5 ,20, 12, 10, 20, 10, 12]
l = [int(x) for x in inp]
print(getSecMax(l))

