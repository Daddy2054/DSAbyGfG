dp = [[-1] * 1001] * 1001


def isSubSequence(s1, s2, i, j):
    if i == 0 or j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + isSubSequence(s1, s2, i - 1, j - 1)
        return dp[i][j]

    else:
        dp[i][j] = isSubSequence(s1, s2, i, j - 1)
        return dp[i][j]


str1 = "gksrek"
str2 = "geeksforgeeks"
m = len(str1)
n = len(str2)

if m > n:
    print("NO")

if isSubSequence(str1, str2, m, n) == m:
    print("YES")

else:
    print("NO")
