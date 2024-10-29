def isPalindrome(s):
    low = 0

    high = len(s)-1

    while low<high:
        if s[low]!=s[high]:
            return False
            break
        low = low+1
        high = high-1
        
    else:
        return True
    

#return s==s[::-1]
isPalindrome("madam")
isPalindrome("hello")