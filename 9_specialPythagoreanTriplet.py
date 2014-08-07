__author__ = 'akhilbhiwal'
import time

"""
A Pythagorean Triplet has following properties:
    -> sum of any 2 sides is always greater than third side.
    -> c**2 = a**2 + b**2
"""
# Returns True if given set of triplet is Pythagorean Triplet else returns False
def isTriplet(a, b, c):
    if a > b and a > c and b + c > a and a ** 2 == b ** 2 + c ** 2:
        return True
    if b > a and b > c and a + c > b and b ** 2 == c ** 2 + a ** 2:
        return True
    if c > a and c > b and a + b > c and c ** 2 == a ** 2 + b ** 2:
        return True
    return False


# Given a number it generates Pythagorean Triplet whose sum is equal to number. Returns False if no such triplet exists. Runtime: O(n)
def findTriplet(finalSum):
    finalSumSquare = finalSum ** 2
    for a in range(int(finalSum / 2), 1, -1):
        b = (finalSumSquare - 2 * finalSum * a) / (2 * N - 2 * a)
        c = N - a - b
        if isTriplet(a, b, c):
            return (a, b, c)
    return False


# Given a number it generates Pythagorean Triplet whose sum is equal to number. Returns False if no such triplet exists. Runtime: O(n**2)
def bruteForceFind(finalSum):
    for a in range(int(finalSum / 2), 1, -1):
        for b in range(int(finalSum / 2), 1, -2):
            c = finalSum - a - b
            if isTriplet(a, b, c):
                return (a, b, c)
    return False


if __name__ == '__main__':
    N = 1000
    a = findTriplet(N)
    if a:
        print a
        print a[0] * a[1] * a[2]
    else:
        print 'No Triplet Exists'

    startTime = time.time()
    findTriplet(N)
    totalTime1 = time.time() - startTime
    print 'Time for running: ' + str(totalTime1)

    # startTime = time.time()
    # bruteForceFind(N)
    # totalTime1 = time.time() - startTime
    # print 'Time for bruteForceFind: ' + str(totalTime1)
