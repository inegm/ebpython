# Eratosthene's sieve
def multiples(list, div):
    for n in list:
        if n % div == 0:
            list.remove(n)
    return list


def apply_sieve(end=120):
    if end > 120:
        raise ValueError('Your end number is too big!')
    all_numbers = range(2, end)
    first = [2, 3, 5, 7]
    for f in first:
        all_numbers = multiples(all_numbers, f)
    primes = first + all_numbers
    return primes
