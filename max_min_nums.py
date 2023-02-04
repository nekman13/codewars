def max_min(numbers):
    lst_int_nums = [int(el) for el in numbers.split(" ")]
    return "%i %i" % (max(lst_int_nums), min(lst_int_nums))


print(max_min("1 3 -5 20 -35 -15 4"))
