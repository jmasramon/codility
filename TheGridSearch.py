#!/bin/python

from monkeyPatchedStdin import raw_input

def solution():
    res = ''
    t = int(raw_input().strip()) # test number
    for a0 in xrange(t):
        R,C = raw_input().strip().split(' ')
        R,C = [int(R),int(C)] # Rows Columns of input Grid
        G = [] # input Grid. Each row an array
        G_i = 0
        for G_i in xrange(R):
            G_t = str(raw_input().strip())
            G.append(G_t)
        r,c = raw_input().strip().split(' ')
        r,c = [int(r),int(c)] # rows columns of test Pattern
        P = [] # test Pattern. Each row an array
        P_i = 0
        for P_i in xrange(r):
            P_t = str(raw_input().strip())
            P.append(P_t)

        foundLines = 0
        lineToCheck = 0
        foundAt = None
        for row in xrange(len(G)):
            # print 'checking', P[lineToCheck]
            # print 'in', G[row]
            if P[lineToCheck] in G[row]:
                foundLines += 1
                if lineToCheck == 0:
                    if R-row < r:
                        print 'NO'
                        res += 'NO/n'
                        break
                    foundAt = G[row].find(P[lineToCheck])
                else:
                    if G[row].find(P[lineToCheck]) != foundAt:
                        print 'NO'
                        res += 'NO/n'
                        break
                    if foundLines == r:
                        print 'YES'
                        res += 'YES/n'
                        break
                lineToCheck += 1
            else:
                foundLines = 0
                lineToCheck = 0
                if row == len(G) - 1:
                    print 'NO'
                    res += 'NO/n'
    return res

print solution()
# assert solution() == 'YES/nNO/nNO/nYES/nYES/nNO/nNO/nYES/nYES/nYES/nYES/n'

