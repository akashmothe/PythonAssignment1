from math import factorial


def prod_of_fact(n):
    res = 1
    for i in range(1,n+1):
        if n%i == 0:
            res *= i
    return res


n = int(input("Enter the number: "))

print(prod_of_fact(n))
