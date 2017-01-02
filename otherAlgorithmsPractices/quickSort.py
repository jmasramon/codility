def partition(A, l, r):
    ll, rr = l-1, r
    u = l
    pivot = A[r]
    print 'starting to pivot with:',A, ll, u, rr, 'pivot:', pivot
    while rr-ll>1:
        if A[u] <= pivot: # should be placed in left group
            ll += 1
            u += 1
        else: # should be placed in right group
            temp = A[u]
            A[u] = A[rr-1]
            A[rr-1] = temp
            rr -= 1 
        print A, ll, u, rr
    if rr != r:
        print 'moving the pivot'
        A[r] = A[rr]
        A[rr] = pivot
        print 'finished pivoting with:', A, ll, u, rr
        return rr
    print 'finished pivoting with:', A, ll, u, rr
    return r 

def partitionClassic(A, l, r): # u last (not in between)
    ll = rr = l
    pivot = A[r]
    
    print 'starting to pivot with:',A, ll, l, rr, 'pivot:', pivot
    for u in xrange(l, r):
        if A[u] <= pivot: # should be placed in left group
            temp = A[u]
            A[u] = A[rr]
            A[rr] = temp
            rr += 1
        u += 1
        print A, ll, u, rr
    if rr > 0 or ((rr == 0) and (ll == 0)):
        print 'moving the pivot'
        A[r] = A[rr]
        A[rr] = pivot
        print 'finished pivoting with:', A, ll, u, rr
        return rr
    print 'finished pivoting with:', A, ll, r-1, rr
    return r 



# print partition([6,3,0,-1,-3,-5],0,5)
# print
# print partition([-5, 0, -1, -3, 6, 3],1,5)

def quickSort(A):
    def loop(A, l, r):
        if (r-l)>0:
            pos = partitionClassic(A, l, r)
            print 'pivot moved to:', pos
            loop(A, l, pos-1)
            loop(A, pos+1, r)
        else:
            return 
    loop(A,0, len(A)-1)
    return A



def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [quickSort]
inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [2,1], [1,1,1], [1,2,1,2,1]]
outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,2], [1,1,1], [1,1,1,2,2]]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
