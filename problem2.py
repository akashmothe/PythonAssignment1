def largest_k_digit(x,k):
    digit = int("9"*k)
    lowest  = digit - int("9"+"0"*(k-1))
    for i in range(digit,lowest,-1):
        if i % x == 0:
            return i
            break

print(largest_k_digit(83,5))