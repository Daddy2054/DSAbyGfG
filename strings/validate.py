def validatePassword(s):
        # code here
        if len(s) < 10:
            return 0
        if not any(char.isupper() for char in s):
            return 0
        if not any(char.islower() for char in s):
            return 0
        if not any(char.isdigit() for char in s):
            return 0
        special_chars = "@#$-*"
        if not any(char in special_chars for char in s):
            return 0
        return 1
