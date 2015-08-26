__author__ = 'jmasramon'

# N is an integer within the range [0..200,000];

def solution(S):
    n = len(S)
    stack = [None]*n
    stack_size = 0

    for i in xrange(n):
       if S[i] == '(' or S[i] == '[' or S[i] == '{':
           stack[stack_size] = S[i]
           stack_size += 1
       elif S[i] == ')' and stack[stack_size - 1] == '(' or  S[i] == ']' and stack[stack_size - 1] == '[' or S[i] == '}' and stack[stack_size - 1] == '{':
           stack_size -= 1
       else:
           return 0
    return 1 if (stack_size == 0) else 0





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
    assert solution("{[()()]}") == 1
    assert solution("([)()]") == 0
    assert solution("") == 1
    assert solution("(") == 0
    assert solution("[") == 0
    assert solution("{") == 0
    assert solution(")") == 0
    assert solution("]") == 0
    assert solution("}") == 0
    assert solution("}]])))") == 0
    assert solution("{{{[[[(((") == 0
