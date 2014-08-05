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

# Returns a list of prime factors of given number.
def get_prime_factors(number):
    arr = []
    for i in range(1, int(number**0.5)):
        if number % i == 0 and is_prime(i):
            arr.append(i)
    if is_prime(number):
        arr.append(number)
    return arr

# Returns prime numbers from 1 to number
def get_primes(number):
    prime_list = []
    for i in range(1, number+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# Returns factor of given number
def get_factors(number):
    factors = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            factors.append(i)
    if is_prime(number):
        factors.append(number)
    return factors


def factors(number):
    prime_list = get_primes(number)
    prime_dict = {}
    for elem in prime_list:
        prime_dict[elem] = 1
    print prime_dict

    for i in range(1, number+1):
        temp = i
        j = 0
        while temp and j < len(prime_list):
            print temp
            if temp % prime_list[j] == 0:
                prime_dict[prime_list[j]] += 1
                temp /= prime_list[j]
                j += 1
            else:
                break
    print prime_dict
    prod = 1
    for elem in prime_dict.keys():
        prod *= elem**prime_dict[elem]
    return prod

def first_n_factors(n):
    all_factors = []
    for i in range(1,n+1):
        all_factors += get_factors(i)
    unique_factors = list(set(all_factors))
    print unique_factors
    prod = 1
    for elem in unique_factors:
        prod *= elem
    return prod

if __name__=='__main__':
#    print [get_prime_factors(i) for i in range(1,20)]
    print factors(10)
#    print first_n_factors(10)