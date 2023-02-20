from gmpy2 import mpz


def sum_strings(x, y):
    return mpz(x or '0') + mpz(y or '0')

print(sum_strings('', 1000_000 * '123'))
