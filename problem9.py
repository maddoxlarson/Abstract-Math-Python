# PROBLEM 9 OF PROJECT EULER.NET
#
# A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,
#                               a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a*b*c.

def pythag_triplet(x):
    triplet=[]
    for i in range(1,x):
        for j in range(1,x):
            for k in range(1,x):
                if (i+j+k==x) and (i**2 + j**2==k**2):
                    return i*j*k

print(pythag_triplet(1000))