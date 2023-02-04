# def encode(st):
#     alfa_list = ['a','e', 'i', 'o', 'u']
#     res_str = ''
#     for symb in st:
#         if symb in alfa_list:
#             code = str(alfa_list.index(symb) + 1)
#         else:
#             code = symb
#         res_str += code
#     return res_str
#
# def decode(st):
#     diction ={
#         '1':'a',
#         '2':'e',
#         '3':'i',
#         '4':'o',
#         '5':'u'
#     }
#     res_str = ''
#     for symb in st:
#         if symb in diction.keys():
#             decode = diction[symb]
#         else:
#             decode = symb
#         res_str += decode
#     return res_str
#
# print(encode('print'))
# print(decode('pr3nt'))

# def encode(s, t=str.maketrans("aeiou", "12345")):
#     return s.translate(t)
#
#
# def decode(s, t=str.maketrans("12345", "aeiou")):
#     return s.translate(t)
#
# print(f"{encode('print')} - {decode('pr3nt')}")
symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
symbols_reverse = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
nums = ""

translation_table = str.maketrans(symbols, symbols_reverse)
translation_table_2 = str.maketrans(symbols_reverse, symbols)


def encode(s):
    return s.translate(translation_table)


def decode(s):
    return s.translate(translation_table_2)


str = input("Введите слово").lower()
print(encode(str), "-", decode(encode(str)))
