__author__ = 'jmasramon'



def firstN(n):
    r = 0
    while r < n:
        yield r
        r += 1

def firstEvenN(n):
    r = 0
    while r < n:
        yield 2*r
        r += 1

import random
def random_DNA_seq(n):
    bases = 'ACGT'
    while(n>0):
        yield random.choice(bases)
        n -= 1

def DNA_seq_all_eq_except_first(n, first, rest):
    yield first
    n -= 1
    while(n>0):
        yield rest
        n -= 1

def DNA_seq_all_eq_except_position(n, exception, position, rest):
    orig_n = n
    while(n>0):
        if n == (orig_n - position):
            print 'yielding exception'
            yield exception
        yield rest
        n -= 1

def DNA_seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while(n>0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                print 'yielding exception'
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


# print random_DNA_seq(50)
# print list(random_DNA_seq(50))
#
# print DNA_seq_all_eq_except_first(50,'A','T')
# print list(DNA_seq_all_eq_except_first(50,'A','T'))
#
# print DNA_seq_all_eq_except_position(50,'A', 5, 'T')
# print list(DNA_seq_all_eq_except_position(50,'A', 5, 'T'))
#
print DNA_seq_all_eq_except_positions(50,['a','c'], [6,13], 'T')
print list(DNA_seq_all_eq_except_positions(50,['a','c'], [6,13], 'T'))

print DNA_seq_all_eq_except_positions(50,[1], [0], 0)
print list(DNA_seq_all_eq_except_positions(50,[1], [0], 0))

print DNA_seq_all_eq_except_positions(50,[4], [0], 3)
print list(DNA_seq_all_eq_except_positions(50,[4], [0], 3))



# print firstN(50)
# print list(firstN(50))
#
# print firstEvenN(50)
# print list(firstEvenN(50))

# print (2 * n for n in range(50))
# print list(2 * n for n in range(50))
