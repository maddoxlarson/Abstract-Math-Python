# PROBLEM 20 OF PROJECT EULER.NET

# Find the sum of the digits in the number 100!.

def factorial(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product

def sum_factorial_digits(n):
    sum=0
    for i in str(factorial(n)):
        sum+=int(i)
    return sum

print(sum_factorial_digits(100))