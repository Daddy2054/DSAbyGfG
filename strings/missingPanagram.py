def missingPanagram(s):
        s = s.lower()
        missing =[]
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabets:
            if char not in s:
                missing.append(char)
        if missing:
            return "".join(missing)  # Convert the list to a string 
        else:
            return -1


print(missingPanagram('The quick brown fox jumps over the lazy dog'))  # Output: q
print(missingPanagram('The quick brown fox jumps over the lazy cat'))  # Output: z