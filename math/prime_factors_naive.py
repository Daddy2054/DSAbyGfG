def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                print(i, end=' ')
                n //= i

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Prime factors of", number, "are:", end=' ')
    prime_factors(number)
