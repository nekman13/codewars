
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

print('Функция выдает', find_even_index([0, 10, -10]))
