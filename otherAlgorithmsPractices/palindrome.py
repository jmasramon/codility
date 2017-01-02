# Check if an array is a palindrome
def palindrome(A):
	# print 'current A:', A
	if len(A) < 2: 
		return True
	if (A[0]!=A[len(A)-1]):
		return False
	A.pop()
	A.pop(0)
	return palindrome(A)


def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [palindrome]
inputs =    [[6,3,0,-1,-3,-5], [6,3,0,0,3,6], [1,2,3,2,1], [2,1], [1,1,1], [1,2,1,2,1]]
outputs =   [False, True, True, False, True, True]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
