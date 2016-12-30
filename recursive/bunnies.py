# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies

def countEarsRecursive(n):
    if n == 1:
        return 2
    else:
        return (2+countEarsRecursive(n-1))

def countEarsIterative(n):
    def loop(n, acc):
        if n == 0:
            return acc
        else:
            return loop(n-1, acc + 2)
    return loop(n, 0)


def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [countEarsRecursive, countEarsIterative]
inputs =    [1,2,3,4,5,6]
outputs =   [2,4,6,8,10,12]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
