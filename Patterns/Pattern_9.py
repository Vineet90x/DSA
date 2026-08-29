#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def pattern(num):
    for i in range(num):
        if i < num//2:
            spaces = num//2 - i
            stars = 2*i - 1
            

        else:
            spaces = i - num//2
            stars = num - 1 - 2 * (i-num//2)
        print(" " * spaces + "*" * stars)
            
pattern(10)