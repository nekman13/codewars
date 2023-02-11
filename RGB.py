def rgb(r, g, b):
    return ''.join([encode(r), encode(g), encode(b)])


def encode(num):
    num = formatted_num(num)
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
    if len(res) == 0:
        res = '00' + res
    elif len(res) == 1:
        res = '0' + res
    return res


def formatted_num(num_source):
    if num_source < 0:
        num_source = 0
    elif num_source > 255:
        num_source = 255
    return num_source


print(rgb(-20, 275, 125))
