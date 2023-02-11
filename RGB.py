def rgb(r, g, b):
    return ''.join([encode(r), encode(g), encode(b)])


def encode(num):
    formatted_num(num)
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


def formatted_num(num_source):
    if num_source < 0:
        num_source = 0
    elif num_source > 255:
        num_source = 255
    return num_source
