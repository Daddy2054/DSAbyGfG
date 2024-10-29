def countVowels(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in s:
            if char.lower() in vowels:
                count += 1
        return count


print(countVowels('Hello World'))  # Output: 3