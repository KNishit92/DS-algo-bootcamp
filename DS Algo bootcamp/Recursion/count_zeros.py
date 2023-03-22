def calcZeros(num, count = 0):
    if num % 10 == 0:
        count += 1
    if num % 10 == num:
        return count
    div, mod = divmod(num, 10)
    return calcZeros(div, count)