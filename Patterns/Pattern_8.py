#*********
# *******
#  *****
#   ***
#    *

def patterns(num):
    for i in range(num // 2):
        spaces = i
        stars = num - 1 - 2*i
        print(" "*spaces+"*"*stars+" "*spaces)
    print()

patterns(10)