__author__ = 'akhilbhiwal'

from prime import is_prime

# Returns sum of all prime numbers of given number
def prime_factors_sum(number):
    arr = []
    for i in range(2, int(number ** 0.5)):
        if number % i == 0 and is_prime(i):
            arr.append(i)
    print arr
    return sum(arr)


if __name__ == '__main__':
    N = 600851475143
    print prime_factors_sum(N)