__author__ = 'jmasramon'
def solution(A):
    # write your code in Python 2.7
    print A
    n = len(A)
    partials = []
    for i in xrange(1,n):
        first = 0
        second = 0
        # print('i',i)
        for j in xrange(i):
          # print('j',j)
          first += A[j]
        # print('first',first)
        for j in xrange(i,n):
            # print('j',j)
            second += A[j]
        # print('second',second)
        partials.append(abs(first-second))
    partials.sort()
    print partials
    return (partials[0])

print solution([3,1,2,4,3])
print solution([-3,-1,-2,-4,-3])
print solution([3,-1,2,-4,3])
print solution([1,2])
print solution([0,2000])
print solution([2000,2000])
print solution([-3,3,-2,2])
print solution([1,3,-2,-3,1])

def fastSolution(A):
    total_sum = sum(A)
    print 'total_sum', total_sum
    partial_sum = 0
    partials = []
    for elem in A[1:]:
        partial_sum += elem
        partials.append(abs(total_sum - 2*partial_sum))
    print partials
    return(min(partials))

print fastSolution([3,1,2,4,3])
print fastSolution([-3,-1,-2,-4,-3])
print fastSolution([3,-1,2,-4,3])
print fastSolution([1,2])
print fastSolution([2000,2000])
print fastSolution([-3,3,-2,2])
print fastSolution([1,3,-2,-3,1])
