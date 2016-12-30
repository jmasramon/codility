# Given n of 1 or more, return the factorial of n,
# which is n * (n-1) * (n-2) ... 1.

def factorialRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * factorialRecursive(n-1)


def factorialIterative(n):
    def loop(n, acc):
        if n == 0:
            return 0
        if n == 1:
            return acc
        else:
            return loop(n-1, acc*n)
    return loop(n, 1)

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [factorialRecursive, factorialIterative]
inputs =    [6,4,0,1,3,5]
outputs =   [720,24,0,1,6,120]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
