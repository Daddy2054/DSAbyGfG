def countVowels(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        distinct = set()
        for char in s:
            if char.lower() in vowels:
                distinct.add(char.lower())
        return distinct.__len__()

print(countVowels('Hello World'))  # Output: 3