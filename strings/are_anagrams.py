def are_anagrams(s1, s2):

        # If lengths are different, they cannot be anagrams
        if len(s1) != len(s2):
            return False

        # Create a dictionary to store character frequencies
        char_count = {}

        # Count frequency of each character in the first string
        for c in s1:
            char_count[c] = char_count.get(c, 0) + 1

        # Decrement frequency of each character in the second string
        for c in s2:

            # If character not found in dictionary or count is zero, return False
            if char_count.get(c, 0) == 0:
                return False
            char_count[c] -= 1

        # Check if all frequencies are zero
        for count in char_count.values():
            if count != 0:
                return False

        # If all conditions satisfied, they are anagrams
        return True


# Test cases
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")

    str1 = "gram"
    str2 = "arm"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")
