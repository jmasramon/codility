def merge(A, B, C):
    # cannot assume A and B of equal len
    # print '  received A,B,C', (A,B,C)
    if B == None:
        return merge(A,C,[])
    n = len(A)
    m = len(B)
    if n == 0:
        C.extend(B)
        # print '    finally returning', C
        return C
    elif m == 0:
        C.extend(A)
        # print '    finally returning', C
        return C
    elif A[0] < B[0]:
        C.append(A.pop(0))
        merge(A,B,C)
    else:
        C.append(B.pop(0))
        merge(A,B,C)
    # print '  returning', C
    return C

def mergeInline(A, left, mid, right):
    # print '  merge inline with (l,m,r)',(left, mid, right)
    acc = []
    i = left
    j = mid + 1
    while (i <= mid and j <= right):
        if A[i] < A[j]:
            acc.append(A[i])
            i+=1
        else:
            acc.append(A[j])
            j+=1
    # print 'after exausting one acc:', acc
    if i<=mid:
        acc.extend(A[i:mid+1])
    else:
        acc.extend(A[j:right+1])
    # print 'acc:', acc
    i=left
    while i<=right:
        A[i] = acc[i-left]
        i+=1
    return A

def mergeSortRecursive(A):
    n = len(A)
    if (n==1):
        return A
    else:
        return merge(mergeSortRecursive(A[:(n/2)]),mergeSortRecursive(A[(n/2):]),[])

def mergeSortRecursiveInline(A):
    def loop(A,l,r):
        # print 'loop wiht (l,r)',(l,r)
        n = r - l
        if (n==0):
            return
        if (n==1):
            # print 'n==1'
            mergeInline(A,l,l,r)
            # print 'A:', A
        else:
            mid = n//2 + l
            # print 'n:', n, 'mid:',mid
            loop(A,l,mid)
            loop(A,mid+1,r)
            mergeInline(A, l, mid, r)
            # print 'A:', A
    loop(A,0,len(A)-1)
    return A

# #########################################################################################

algorithms = [mergeSortRecursive, mergeSortRecursiveInline]
inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [2,1], [1,1,1], [1,2,1,2,1]]
outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,2], [1,1,1], [1,1,1,2,2]]

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

def get_unsorted_list(size):
    return [random.randint(0,1000000) for i in xrange(size)]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
    random_lists = get_unsorted_list(10)
