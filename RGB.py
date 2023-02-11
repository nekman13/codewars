def rgb(r, g, b):
    return(''.join([encode(r), encode(g), encode(b)]))


def encode(num):
    if num < 0:
        num = 0
    elif num > 255:
        num = 255
    list_code = ['A', 'B', 'C', 'D', 'E', 'F']
    res = ''
    while num > 0:
        mod = num % 16
        if mod > 9:
            mod = list_code[mod % 10]
        else:
            mod = str(mod)
        res = str(mod) + res
        num = num // 16
    return res
