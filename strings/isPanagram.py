def isPanagram(s):
        s = s.lower()
        letters = set()
        for char in s:
            if char.isalpha():
                letters.add(char)
        return len(letters) == 26

print(isPanagram('The quick brown fox jumps over the lazy dog'))  # Output: True    
print(isPanagram('The quick brown fox jumps over the lazy cat'))  # Output: False   