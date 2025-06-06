from string import printable, ascii_lowercase

#для основания <= 10
def con(x, n):
    res = []
    while x > 0:
        res = [x%n] + res
        x //= n
    return res

#для основания > 10 и < 36 
def conv(x, n):
    res = ''
    while x > 0:
        res = str(printable[x%n]) + res
        x //= n
    return res