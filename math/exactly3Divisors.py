def exactly3Divisors(N):
    count = 0
    for i in range(2, N + 1):
        divisorCount = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    divisorCount += 1
                else:
                    divisorCount += 2
        if divisorCount == 3:
            count += 1
    return count

print(exactly3Divisors(6))