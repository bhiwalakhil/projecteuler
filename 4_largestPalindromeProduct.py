__author__ = 'akhilbhiwal'

# Returns the largest palindrome formed from N digit numbers
def palindrome(digits):
    largest = 10**digits - 1
    max_prod = 0

    # j_min stores the smallest value for number 2.
    j_min = 0
    for i in range(largest, 1, -1):
        for j in range(largest, j_min, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > max_prod:
                    max_prod = product
                j_min = j
                break
    return max_prod

if __name__=='__main__':
    # N is the number of digits. N =3 represents a three digit number
    N = 3
    print palindrome(N)