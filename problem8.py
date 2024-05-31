# PROBLEM 8 OF PROJECT EULER.NET

# The four adjacent digits in the 1000-digit number that have the greatest product are 9*9*8*9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

number=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# number_as_string=str(number)
# number_as_list=[int(i) for i in number_as_string]
# number_digits=len(number_as_list)


# def all_nines(x):
#     lst=[]
#     for i in str(x):
#         for j in range(1,14):
#             if int(i)==9 and j==9:
#                 lst.append(1)
#     print(max(lst))

def multiply_all(x):
    product=1
    number_as_list=[int(i) for i in str(x)]
    for digit in range(1,len(number_as_list)):
        product*=digit
        for i in range(0,14):
            if digit-i<13:
                product*=number_as_list[digit+i]
            else:
                product+=1
    return product

print(multiply_all(number))

# for i in range(len(number_as_string)):
#     product=1
#     for j in range(1,14):
#         product*=int(number_as_string[i+j])

# def int_to_list(x):
#     lst=list()
#     for i in str(x):
#         lst.append(int(i))
#     return lst

# def thirteenth_product(x):
#     product=1
#     for i in range(len(int_to_list(x))):
#         if len(int_to_list(x))-i>=13:
#             for j in range(0,14):
#                 product*=int_to_list(x)[i+j]
#         else:
#             product*=1
#     return product

# def max_thirteenth_product(x):
#     return max(map(thirteenth_product, int_to_list(x)))

# print(max_thirteenth_product(number))