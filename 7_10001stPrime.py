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

if __name__=='__main__':
    count,i = 0,1
    N = 10001
    while count != N:
        i += 1
        if is_prime(i):
            count += 1

    print i
