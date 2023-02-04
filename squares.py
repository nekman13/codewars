def squares(num):
    result = ""
    for numb in str(num):
        result += str(int(numb) ** 2)
    return int(result)


print(squares(9119))
print(squares(10000))