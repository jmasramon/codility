__author__ = 'jmasramon'

def solution(X, A): # A = fallen leaves. Index is time, value is position
    fallen = [None]*X
    for ind, elem in A:
        if fallen[elem-1] == 0:
            fallen[elem-1] = 1
            if sum(fallen) == X: return ind


assert solution([1,3,1,4,2,3,5,4]) == 6
