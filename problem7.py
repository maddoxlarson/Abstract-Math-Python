# PROBLEM 7 OF PROJECT EULER.NET
#
# Find the 10,001st prime number.
# Solution from @SuperBiasedMan on Stack Overflow, link below.
# https://codereview.stackexchange.com/questions/102507/finding-the-10001st-prime

# def is_prime(n): # check if n is prime : return Boolean
#     if n<=1: return False
#     else:
#         if all(map(lambda i: n%i != 0, range(2,n))): return True
#         else: return False

def find_nth_prime(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

print(find_nth_prime(10001))