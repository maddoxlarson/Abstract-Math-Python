# PROBLEM 1 OF PROJECT EULER.NET

# Find the sum of all multiples of 3 or 5 below 1000.

J=[]

def SortingProcess():
    for i in range(1000):
        if i%3==0: # if a given number between 0 and 1000 is divisible by 3, then add it to the list.
            J.append(i)
        elif i%5==0: # if a given number between 0 and 1000 is divisible by 5, then add it to the list.
            J.append(i)

def SumList(lst):
    sum = 0
    for i in lst: # add together the multiples of 3 and 5 that are less than 1000.
        sum+=i
    print(sum)

SortingProcess()
SumList(J)
