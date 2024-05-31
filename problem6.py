# PROBLEM 6 OF PROJECT EULER.NET

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(x):
    sum=0
    for i in range(1,x+1):
        sum+=i**2
    return sum

def square_of_sum(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    sum*=sum
    return sum

n=int(input('Find the difference between the sum of the squares of the first ___ natural numbers and the square of the sum.'))
print(square_of_sum(n)-sum_of_squares(n))