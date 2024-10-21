def nonrepeatingCharacter(s):
    # Code  
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                # print(d)
        for i in s:
            if d[i] == 1:
                return i
        return "$"   
print(nonrepeatingCharacter("hello"))
print(nonrepeatingCharacter("abcab"))
print(nonrepeatingCharacter("aabbcc"))