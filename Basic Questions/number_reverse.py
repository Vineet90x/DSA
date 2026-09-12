#REVERSING A NUMBER

num = 12345
rev = 0

while num > 0:
    print(num,rev)
    last = num % 10
    rev = rev*10+last 
    num = num // 10
    print(num)
print(rev)