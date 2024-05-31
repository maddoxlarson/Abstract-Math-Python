

def is_prime(n): # check if n is prime : return Boolean
    if n<=1: return False
    else:
        if all(map(lambda i: n%i != 0, range(2,n))): return True
        else: return False

def list_primes(n):
    # list primes up to n
    lst=[i for i in range(2,n) if is_prime(i)]
    return lst

def sum_primes(n):
    sum=0
    for i in list_primes(n):
        sum+=i
    return sum

print(sum_primes(2000000))