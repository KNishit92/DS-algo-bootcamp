import math
def reverseDigits(num):
    if num % 10 == num:
        return num
    dig = int(math.log10(num))
    div, mod = divmod(num, 10)
    return mod * pow(10, dig) + reverseDigits(div)
    
print(reverseDigits(1200))