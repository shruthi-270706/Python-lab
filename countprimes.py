import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

args = [int(x) for x in sys.argv[1:]]
prime_numbers = [num for num in args if is_prime(num)]

print("Count of prime numbers:", len(prime_numbers))
print("Prime numbers:", *prime_numbers)
