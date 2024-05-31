# PROBLEM 3 OF PROJECT EULER.NET

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    rev_num_string = str(n)[::-1]
    if int(rev_num_string)==n:
        return True
    else:
        return False

def three_digit_numbers():
    lst=[]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if int(str(i)+str(j)+str(k))>99:
                    lst.append(int(str(i)+str(j)+str(k)))
    new_lst=[]
    for i in lst:
        for j in lst:
            if is_palindrome(i*j):
                new_lst.append(i*j)
    
    print(sorted(new_lst)[-1])

three_digit_numbers()