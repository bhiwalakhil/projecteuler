import operator
import cProfile

def multiples(arg1, arg2, rangeValue):
    arr = []
    for i in range(arg1, rangeValue, arg1):
        arr.append(i)
    for i in range(arg2, rangeValue, arg2):
        if i not in arr:
            arr.append(i)
    # print arr
    return sum(arr)

def multiples2(arg1, arg2, rangeValue):
    arr = []
    i,j = 0,0
    while i < rangeValue or j < rangeValue:
        if (i % arg1 == 0) and (i < rangeValue):
            if i not in arr:
                arr.append(i)
        if (j% arg2 == 0) and (j < rangeValue):
            if j not in arr:
                arr.append(j)
        i = i + arg1
        j = j + arg2
    # print sorted(arr)
    return sum(arr)


if __name__ == '__main__':
    # t = timeit.Timer("""multiples(3, 5, 10000)""", setup="""x=range(1000)""" )
    # t2 = timeit.Timer("""multiples2(3, 5, 10000)""", setup="""x=range(1000)""" )
    #
    # print t.timeit(), t2.timeit()
    cProfile.run('multiples(3, 5, 100000)')
    cProfile.run('multiples2(3, 5, 100000)')
