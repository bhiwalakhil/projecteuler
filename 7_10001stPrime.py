__author__ = 'akhilbhiwal'

from prime import is_prime

if __name__ == '__main__':
    count, i = 0, 1
    N = 10001
    while count != N:
        i += 1
        if is_prime(i):
            count += 1

    print i
