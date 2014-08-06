__author__ = 'akhilbhiwal'

from random import randrange

def generate(digits):
    upperLimit = 10**(digits) - 1
    lowerLimit = 10**(digits-1)
    return randrange(lowerLimit, upperLimit)

# if __name__=='__main__':
#     print generate(100000)