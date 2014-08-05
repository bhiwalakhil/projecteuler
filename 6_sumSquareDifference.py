__author__ = 'akhilbhiwal'

def sumSquareDifference(N):
    sumSquare = 0

    for i in range(1, N+1):
        sumSquare += i*i

    productOfSum = (N*(N+1)/2) ** 2

    return productOfSum - sumSquare

if __name__=='__main__':
    N = 100
    print sumSquareDifference(N)