def merge(A, B, C):
    # cannot assume A and B of equal len
    print '  received A,B,C', (A,B,C)
    if B == None:
        return merge(A,C,[])
    n = len(A)
    m = len(B)
    if n == 0:
        C.extend(B)
        return C
    elif m == 0:
        C.extend(A)
        return C
    elif A[0] < B[0]:
        C.append(A.pop(0))
        merge(A,B,C)
    else:
        C.append(B.pop(0))
        merge(A,B,C)
    print '  returning', C
    return C

def mergeSort(A):
    def loop(A, res):
        n = len(A)
        if (n>1):
            (B,C) = (A[:(n/2)],A[(n/2):])
            print 'temp vectors B,C:', (B,C)
            res = merge(loop(B, res),loop(C, res), res)
        else:
            print 'simply returning A:', A
            return A
    res = []
    loop(A, res)
    return res

print mergeSort([6,3,0,-1,-3,-5])


# def myAssert(func, inp, e_res):
#     res = func(inp)
#     try:
#         assert res == e_res
#         return '\033[92m' + 'OK' + '\033[0m'
#     except AssertionError, e:
#         return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

# algorithms = [mergeSort]
# inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [2,1], [1,1,1], [1,2,1,2,1]]
# outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,2], [1,1,1], [1,1,1,2,2]]

# if __name__ == '__main__':
#     print 'Start tests..'
#     print len(algorithms), 'algorithms to test'
#     print len(inputs), 'tests to conduct'
#     for i in range(len(algorithms)):
#         print 'testing alg:', algorithms[i]
#         for j in range(len(inputs)):
#             print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
