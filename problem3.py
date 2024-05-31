# PROBLEM 3 OF PROJECT EULER.NET

# Find the largest primce factor of 600851475143.

import math

def is_prime(n): # check in n is prime : return Boolean
    if n<=1:
        return False
    for i in range(2,n): # if n is divisible by any lower number, return false
        if n%i==0:
            return False
    return True

def prime_factors(n): # find list of prime factors : return List
    factors=[]
    if is_prime(n):
        return n
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0 and is_prime(i):
                factors.append(i)
    # print(factors)
    return factors

def largest_prime_factor(n): # return largest prime factor: return Integer
    factors_of_n=list(prime_factors(n))
    return factors_of_n[-1]

number=600851475143
print(largest_prime_factor(600851475143))