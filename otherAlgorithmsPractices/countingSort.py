
def countNumbers(A,m):
    B = [0]*m
    for i in xrange(len(A)):
        B[A[i]] += 1
    return B

def countBefores(A,m):
    B = [0]*m
    for i in xrange(1,m):
        B[i] = B[i-1] + A[i-1]
    return B

def countingSort((A,m)):
    numbers = countNumbers(A,m)
    print "numbers:", numbers
    befores = countBefores(numbers,m)
    print "befores:", befores

    B = [0]*len(A)
    p = 0
    for i in xrange(1,m):
        for j in xrange(befores[i] - befores[i-1]):
            print "befores[i]:",befores[i]
            B[p] = i-1
            print B
            p += 1
    for i in xrange(p,len(A)):
        B[i] = m-1
        print B
    return B



# ##############################################################

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [countingSort]
inputs =    [([4,1,5,0,1,6,5,1,5,3],7)]
outputs =   [[0,1,1,1,3,4,5,5,5,6]]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
