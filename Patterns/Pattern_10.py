# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def pattern(num):
    for i in range(num):
        if i < num // 2:
            stars = i+1
        else:
            stars = num - i
        print("*"*stars)
pattern(10)