__author__ = 'jmasramon'

def solution(A):
    n = len(A)
    reversed = [None]*n
    for i, elem in enumerate(A):
        reversed[n-(i + 1)] = elem
    return reversed

def betterSolution(A):
    n = len(A)
    for i in xrange(n//2):
        j =  n - (i +1)
        A[i], A[j] =  A[j], A[i] # swap variables with tuple assignment
    return A

if __name__ == '__main__':
    print 'Start tests..'
    print solution([1,2,3,4])
    print betterSolution([1,2,3,4])
