__author__ = 'jmasramon'

import timeit

def sumatorial(n):
    start = timeit.default_timer()
    i=n
    total=0
    while(i):
        total += i
        i -= 1
    stop = timeit.default_timer()
    print 'time spent:', stop - start
    return total

print 'mine'
assert(sumatorial(2) == 3)
assert(sumatorial(4) == 10)
assert(sumatorial(5) == 15)
assert(sumatorial(6) == 21)
assert(sumatorial(1000) == 500500)

def slow_solution(n):
    start = timeit.default_timer()
    result = 0
    for i in xrange(n):
        for j in xrange(i + 1):
            result += 1
    stop = timeit.default_timer()
    print 'time spent:', stop - start
    return result

print 'slow'
assert(slow_solution(2) == 3)
assert(slow_solution(4) == 10)
assert(slow_solution(5) == 15)
assert(slow_solution(6) == 21)
assert(slow_solution(1000) == 500500)


def model_solution(n):
    start = timeit.default_timer()

    res = n * (n+1) // 2

    stop = timeit.default_timer()
    print 'time spent:', stop - start

    return res

print 'model'
assert(model_solution(2) == 3)
assert(model_solution(4) == 10)
assert(model_solution(5) == 15)
assert(model_solution(6) == 21)
assert(model_solution(1000) == 500500)
