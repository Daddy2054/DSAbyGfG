def printNto1(n):
    if n <= 0:
        return
    print(n)
    printNto1(n - 1)


n = 3
printNto1(n)
