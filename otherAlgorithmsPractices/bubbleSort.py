def bubbleSort(A):
    B = A[:]
    n = len(A)
    not_sorted = True
    # print 'input:', A

    while not_sorted:
        not_sorted = False
        for j in range(n-1):
            for i in range(n-j-1):
                if B[i] > B[i+1]:
                    not_sorted = True
                    temp = B[i+1]
                    B[i+1] = B[i]
                    B[i] = temp

    return B

def bubbleSortByBook(A):
    B = A[:]
    n = len(A)

    # print 'input:', A
    for i in range(n-1):
        # print 'i:', i
        for j in range(n-i-1):
            # print '  j:', j
            if B[j] > B[j+1]:
                temp = B[j+1]
                B[j+1] = B[j]
                B[j] = temp
            # print '    temp res:', B

    return B


def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

def assertBubbleSort(inp, e_res):
    myAssert(bubbleSort, inp, e_res)

algorithms = [bubbleSort, bubbleSortByBook]
inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [1,1,1], [1,2,1,2,1]]
outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,1,1], [1,1,1,2,2]]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])

