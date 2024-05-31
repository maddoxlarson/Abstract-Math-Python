# PROBLEM 2 OF PROJECT EULER.NET

# Find the sum of even Fibonacci numbers < 4x10^6.

import math

F=[] # set of Fibonacci numbers
E=[] # even Fibs
golden_ratio=0.5+ math.sqrt(5)/2
conjugate=1-golden_ratio

def fibonacci_number(n): # find nth Fibonacci number
    fib = (golden_ratio**n - conjugate**n)/math.sqrt(5)
    return fib

def add_to_fib_seq(): # add the Fib numbers less than 4x10^6 to the list F
    for i in range(70):
        if fibonacci_number(i)<4000000:
            F.append(round(fibonacci_number(i),0))

def remove_from_fib(): # remove the even Fib numbers from F and add them to E
    add_to_fib_seq()
    for i in F:
        if i%2==0:
            F.remove(i)
            E.append(i)

def sum_if_even(): # sum the even Fib numbers in list E then print
    # add_to_fib_seq()
    remove_from_fib()
    sum=0
    for i in E:
        sum+=i
    print(sum)

sum_if_even()