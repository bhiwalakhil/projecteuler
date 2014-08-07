__author__ = 'akhilbhiwal'

from prime import is_prime


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def getPrimeSum(N):
    total = 2
    for next_prime in get_primes(3):
        if next_prime < N:
            total += next_prime
        else:
            return total


if __name__ == '__main__':
    N = 2000000
    print getPrimeSum(N)
