def fact_of_product(x):
    prod = 1
    fact = []
    for i in x:
        prod *= i
    for i in range(1,prod+1):
        if prod%i == 0:
            fact.append(i)
    return fact, len(fact)


a = list(map(int,input("Enter space separated values: ").split()))
print(fact_of_product(a))
