# PROBLEM 14 OF PROJECT EULER.NET

# Which starting number under 10^6 has the longest Collatz string?

# DEFINITION OF THE PROCEDURE
def collatz(z): # iterate a number z through the Collatz procedure until it terminates in 1.
    lst=[]
    lst.append(int(z))
    while z >= 1:
        if z%2==0: z/=2
        elif z%2==1: z=3*z+1
        lst.append(int(z))
        if lst[-1]==1: break
    return lst

# RETURN LENGTH OF LONGEST STRING
def longest_string(x): # iterate though x and find longest seq : return len of longest
    num=0
    greatest=0
    for i in range(x):
        c=len(collatz(i))
        if num<c:
            num=c
            greatest=i
    return greatest

print(longest_string(1000000))