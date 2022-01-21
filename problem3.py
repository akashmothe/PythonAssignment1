
def smallest_k_digit(x,k):
    digit = int("1"+"0"*(k-1))
    largest = int("9"*k)
    for i in range(digit,largest):
        if i % x == 0:
            return i
            break

print(smallest_k_digit(83,5))