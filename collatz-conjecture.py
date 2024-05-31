# A LAYMAN'S ATTEMPT TO ADDRESS THE COLLATZ CONJECTURE

import matplotlib.pyplot as plt
import numpy as np

# DEFINITION OF THE PROCEDURE

def collatz(z): # iterate a number z through the Collatz procedure until it terminates in 4,2,1
    lst=[]
    lst.append(int(z))
    while z >= 1:
        if z%2==0: z/=2
        elif z%2==1: z=3*z+1
        lst.append(int(z))
        if lst[-1]==1: break
    return lst

# CHECK IF THE FIRST n NUMBERS TERMINATE IN THE DESIRED SEQUENCE?
# def is_collatz_loop(x):
#     collatz_string=collatz(x)
#     if collatz_string[-1]==1:# and collatz_string[-2]==2 and collatz_string[-3]==4:
#         return True
#     else:
#         return False
# def check_first_m(m):
#     for i in range(2,m):
#         print('Does ' + str(i) + ' terminate in the 1,2,4 loop?: ' + str(is_collatz_loop(i)))
# check_first_m(1000)

# GRAPH OF THE FIRST N NATURAL NUMBERS

plt.figure()

iterator=1
n=5
while iterator<n:
    collatz_matrix=[collatz(number) for number in list(range(1,n+1))] # create a matrix of Collatz strings
    x = np.array(list(range(int(len(collatz_matrix[iterator-1]))))) # x-axis is number of iterations before reached 1
    y = np.array(collatz_matrix[iterator-1]) # y-axis is the value after each iteration
    plt.scatter(x,y,color='r')
    plt.plot(x,y,'r-',label='Collatz string: ' + str(collatz_matrix[iterator-1][0])) # create lines so that you can see where each string starts/ends
    iterator+=1

plt.ylabel('f(n)')
plt.xlabel('n')

xlabels=[str(x) for x in range(1,n*2)]
ylabels=[str(x) for x in range(1,(n**2)-6)]

plt.xticks(list(range(1,n*2)),xlabels)
plt.yticks(list(range(1,(n**2)-6)),ylabels)

plt.title('n iterations of Collatz procedure')

plt.legend()
plt.show()
