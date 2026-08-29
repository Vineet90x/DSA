# remainder

# print(7789 % 10)
# print(778 % 10)
# print(77 % 10)
# print(7 % 10)
# print(0 % 10)

# quotient

# print(77 // 2)

# given the number n find out and return the number of digits present in a number.

def digits(num):
    count = 0
    num = abs(num)
    if num == 0:
        return 1
    while (num > 0):
        count +=1
        num = num // 10
    return count

print(digits(-2320))