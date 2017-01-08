
def fibonacciRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)

def fibonacciIte(n):
    def loop(n, n1, n2):
        if n == 0:
            return n2
        else:
            return loop(n-1, n1+n2, n1)
    return loop(n,1,0)

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [fibonacciIte, fibonacciRec]
inputs =    [0,1,2,3,4,5,6,7,100]
outputs =   [0,1,1,2,3,5,8,13,354224848179261915075]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
