# PROBLEM 16 OF PROJECT EULER.NET

# What is the sum of the digits of the number 2^1000?

def raise_to_two(x):
    return 2**x

def sum_digits(x):
    as_string=str(raise_to_two(x))
    sum=0
    for i in range(0, len(as_string)):
        sum+=int(as_string[i])
    return sum

# num=int(input('Enter a number: '))

print(sum_digits(1000))
