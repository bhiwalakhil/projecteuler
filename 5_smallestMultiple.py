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

# Returns a list of prime numbers from 1 to number
def get_primes(number):
    prime_list = []
    for i in range(1, number+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# Returns a dictionary of prime factors passed as an argument.
def get_prime_factors(number, prime_numbers_list, smallest_multiple_dict):
    prime_factors = []
    i = 0
    # finds all prime factor of number and add them to prime_factors list
    while i < len(prime_numbers_list):
        if number % prime_numbers_list[i] == 0:
            prime_factors.append(prime_numbers_list[i])
            number = number/prime_numbers_list[i]
            if number == 1:
                break
        else:
            i += 1

    # updates the dictionary with count of prime factors
    j = 0
    while j < len(prime_factors):
        num_count = prime_factors.count(prime_factors[j])
        if num_count > smallest_multiple_dict.get(prime_factors[j]):
            smallest_multiple_dict[prime_factors[j]] = num_count
        j = j+num_count
    return smallest_multiple_dict

# Computes the smallest positive number which is evenly divisible by all number from 1 to N
def smallesMultiple(N):
    # smallest_multiple_dict stores count of prime numbers
    smallest_multiple_dict = {}
    prime_numbers_list = get_primes(N)

    for i in range(2, N+1):
        smallest_multiple_dict = get_prime_factors(i, prime_numbers_list, smallest_multiple_dict)


    multiple = 1
    for key in smallest_multiple_dict.keys():
        multiple *= key ** smallest_multiple_dict[key]

    return multiple

if __name__=='__main__':
    N = 10
    print smallesMultiple(N)