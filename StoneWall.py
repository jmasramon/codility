__author__ = 'jmasramon'



# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular).
# Your task is to compute the minimum number of blocks needed to build the wall

# notes:
# if same heigth for a while -> same block
# if height does not fall under last block -> same block as base but can have other blocks over it
# so: if < or > -> new block  if < or > and = -> no new block

def solution(H):
    n = len(H)
    num = 0
    stack = [None]*n
    stack_size = 0

    if n == 0:
        return 0

    num +=1
    stack[stack_size] = H[0]
    stack_size += 1

    print 'We begin with:', H, stack, stack_size, num
    print

    for i in xrange(1,n):
        print i, H[i], stack, stack_size, stack[stack_size-1], num
        while stack_size >= 1 and H[i] < stack[stack_size-1]:
            print 'reducing stack'
            stack_size -= 1
        if H[i] > stack[stack_size-1]:
            print 'new kids on the block'
            num += 1
            stack[stack_size] = H[i]
            stack_size += 1
        print 'input:', i, H[i], 'output:', stack_size, stack[stack_size-1]
    return num




def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while (n > 0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1

if __name__ == '__main__':
    print 'Start tests..'
    assert solution([]) == 0
    assert solution([6]) == 1
    assert solution([6,7]) == 2
    print
    assert solution([8,8,5,7,9,8,7,4,8]) == 7

