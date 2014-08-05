__author__ = 'kaushikn'
import cProfile

def FibonnaciSum(limit):
    num1 = 1
    num2 = 2
    sum = 2
    temp = 0
    while temp < limit:
        temp = num1 + num2
        num1 = num2
        num2 = temp
        if temp % 2 == 0:
            sum += temp
    return sum

def RecursiveFibonnaciSum(num1, num2, limit):
    if num1+num2 < limit:
        if num1 % 2 == 0:
            return num1 + RecursiveFibonnaciSum(num2, num1+num2, limit)
        else:
            return 0 + RecursiveFibonnaciSum(num2, num1+num2, limit)
    else:
        if num1 % 2 == 0:
            return num1
        elif num2 % 2 == 0:
            return num2
        else:
            return 0

if __name__=='__main__':
    print cProfile.run('FibonnaciSum(4000000)')
    print cProfile.run('RecursiveFibonnaciSum(1,2,4000000)')