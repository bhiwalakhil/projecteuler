__author__ = 'akhilbhiwal'

# Returns True if given number is prime else returns False
def is_prime(number):
    if number <=3:
        if number <= 1:
            return False
        return True
    if not number % 2 or not number %3:
        return False
    for i in range(5, int(number**0.5) + 1, 6):
        if not number % i or not number % (i+2):
            return False
    return True

# Returns sum of all prime numbers of given number
def prime_factors_sum(number):
    arr = []
    for i in range(2, int(number**0.5)):
        if number % i == 0 and is_prime(i):
            arr.append(i)
    print arr
    return sum(arr)

if __name__=='__main__':
    N = 600851475143
    print prime_factors_sum(N)