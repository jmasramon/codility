def fibbonaciRecursive(n):
    if n < 2:
        return n
    return fibbonaciRecursive(n-1) + fibbonaciRecursive(n-2)

def fibbonaciIterative(n):
    def loop(n, prvv, prev):
        if n == 0:
            return 0
        if n == 1:
            return prev
        return loop(n-1, prev, prvv + prev)
    return loop(n, 0, 1)


def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [fibbonaciRecursive, fibbonaciIterative]
inputs =    [0,1,2,3,4,5,6]
outputs =   [0,1,1,2,3,5,8,13]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
