# PROBLEM 5 OF PROJECT EULER.NET
#
# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
#
# Solution from @aris on Stack Overflow, link below.
# https://stackoverflow.com/questions/22711505/smallest-positive-number-that-is-evenly-divisible-by-all-of-the-numbers-from-1-t

from itertools import count, takewhile

def primes(n):
    # Generate prime numbers up to n
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            return i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result

print(smallest(20))
# print(primes(10))