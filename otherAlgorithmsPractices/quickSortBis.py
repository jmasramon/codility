def partition(A,l,r):
    L = l
    pivot = A[r]
    # print "partitioning A:",A
    if l==r:
        return A
    else:
        for i in xrange(l, r):
            if A[i] < pivot:
                temp = A[L]
                A[L] = A[i]
                A[i] = temp
                L += 1
        if L<r:
            temp = A[L]
            A[L] = pivot
            A[r] = temp
        # print "Partitioned A:", A
        if L-1>l:
            # print "repartitioning to the left of L:", L
            partition(A,l,L-1)
        if L+1 < r:
            # print "repartitioning to the right of L:", L
            partition(A,L+1,r)
        return A

def quickSort(A):
    if len(A)>1:
        partition(A,0,len(A)-1)
    return A

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [quickSort]
inputs =    [[-5,-3,-1,0,3,6], [6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [2,1], [1,1,1], [1,2,1,2,1]]
outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,2], [1,1,1], [1,1,1,2,2]]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
