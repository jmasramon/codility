__author__ = 'jmasramon'


# A, C, G and T  impact factors of 1, 2, 3 and 4, respectively
# What is the minimal impact factor of nucleotides contained in a particular part
# of the given DNA sequence?


# todo finish with https://codility.com/demo/results/demo3J3SM6-PE5/
def solution(S, P, Q):
    n = len(S)
    m = len(P)
    imp_fact = {'A':1, 'C':2, 'G':3, 'T':4}
    res = [5]*m
    for i in xrange(m):
        # print 'i =',i
        if P[i] == Q[i]:
            res[i] = imp_fact[S[P[i]]]
        for j in xrange(P[i], Q[i]):
            if imp_fact[S[j]] < res[i]:
                res[i] = imp_fact[S[j]]
            # print 'j =', j, 'res[i] =', res[i]
    return res

def faster_solution(S, P, Q):
    n = len(S)
    m = len(P)
    imp_fact = {'A':1, 'C':2, 'G':3, 'T':4}
    res = [5]*m
    impacts = [0]*n
    for i in xrange(n):
        impacts[i] = imp_fact[S[i]]
    # print S,'->',impacts

    for i in xrange(m):
        # print 'i =',i
        if P[i] == Q[i]:
            res[i] = impacts[P[i]]
        for j in xrange(P[i], Q[i]):
            if impacts[j] == 1:
                res[i] = 1
                break
            if impacts[j] < res[i]:
                res[i] = impacts[j]
            # print 'j =', j, 'res[i] =', res[i]
    return res

def prefix_sums(A):
    n = len(A)
    pr_sums = [0]*(n+1)
    for i in xrange(1, n+1):
        pr_sums[i] = pr_sums[i-1] + A[i-1]
    return pr_sums

def count_total(P,x,y):
    # print P, x, y
    return P[y+1] - P[x]

def DNA_seq_all_eq_except_position(n, exception, position, rest):
    orig_n = n
    while(n>0):
        if n == (orig_n - position):
            # print 'yielding exception'
            yield exception
        yield rest
        n -= 1

def DNA_seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while(n>0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                # print 'yielding exception'
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


assert faster_solution('CAGCCTA',[2,5,0], [4,5,6]) == [2, 4, 1]
assert faster_solution('C',[0], [0]) == [2]
assert faster_solution('C',[0,0,0], [0,0,0]) == [2, 2, 2]
assert faster_solution('TTC',[0,1,2], [1,1,2]) == [4, 4, 2]
assert faster_solution('GGGGGGTGGGGGGCGGGGGG',[0,1,2,0,6], [1,1,2,20,6]) == [3, 3, 3, 2, 4]
# print faster_solution(list(DNA_seq_all_eq_except_positions(50,['T','C'], [6,13], 'G')), [0,1,2,0,6], [1,1,2,20,6])
assert faster_solution(list(DNA_seq_all_eq_except_positions(50,['T','C'], [6,13], 'G')), [0,1,2,0,6], [1,1,2,20,6]) == [3, 3, 3, 2, 4]
# print faster_solution(list(DNA_seq_all_eq_except_position(50,'T',6,'G')), [0,1,2,0,6], [1,1,2,20,6])
assert faster_solution(list(DNA_seq_all_eq_except_position(50,'T',6,'G')), [0,1,2,0,6], [1,1,2,20,6]) == [3, 3, 3, 3, 4]
assert faster_solution(list(DNA_seq_all_eq_except_positions(100000,['T','C'], [6,13], 'G')), [0,1,2,0,6], [1,1,2,20,6]) == [3, 3, 3, 2, 4]
print faster_solution(list(DNA_seq_all_eq_except_positions(100000,['T'], [0], 'G')), list(DNA_seq_all_eq_except_positions(50,[1], [0], 0)), list(DNA_seq_all_eq_except_positions(50,[1], [0], 0)))
# assert faster_solution(list(DNA_seq_all_eq_except_positions(100000,['T'], [0], 'G')), list(DNA_seq_all_eq_except_positions(50,[1], [0], 0)), list(DNA_seq_all_eq_except_positions(50,[1], [0], 0))) == list(DNA_seq_all_eq_except_positions(50,[4], [0], 3))


# print primesSmallerThanN('CAGCCTA',[2,5,0], [4,5,6])
assert solution('CAGCCTA',[2,5,0], [4,5,6]) == [2, 4, 1]
assert solution('C',[0], [0]) == [2]
assert solution('C',[0,0,0], [0,0,0]) == [2, 2, 2]
assert solution('TTC',[0,1,2], [1,1,2]) == [4, 4, 2]
assert solution('GGGGGGTGGGGGGCGGGGGG',[0,1,2,0,6], [1,1,2,20,6]) == [3, 3, 3, 2, 4]
