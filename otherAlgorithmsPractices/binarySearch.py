def linearSearch(params):
    (A, a) = params
    for i in xrange(len(A)):
        if (A[i]==a):
            return i
    return

def binarySearch(params):
    (A, a) = params
    l, r = 0, len(A)
    while l<r:
        half = (l+r)//2
        # print (l,half, r, A[half])
        if A[half] == a:
            return half
        elif A[half] < a:
            l = half
        else:
            r = half
    return

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [linearSearch, binarySearch]
inputs =    [([-5,-3,-1,0,3,6], -1), 
                ([-5,-3,-1,0,3,6], 3), 
                ([-5,-3,-1,0,3,6], -5), 
                ([-5,-3,-1,0,3,6], 0)]
outputs =   [2, 4, 0, 3]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
