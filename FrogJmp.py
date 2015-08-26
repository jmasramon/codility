__author__ = 'jmasramon'

# inital_pos <= final_pos
# jump_dist


def min_num_jumps(fr, to, jd):
    print 'div:', (to-fr)/jd, 'mod:', (to-fr)%jd , 'tot:', (to-fr)/jd + (to-fr)%jd
    return (to-fr)/jd + (1 if (to-fr)%jd else 0)




print(min_num_jumps(1,1, 2))
assert(min_num_jumps(1,1, 2) == 0)
print(min_num_jumps(1,2, 2))
assert(min_num_jumps(1,2, 2) == 1)
print(min_num_jumps(1,4, 2))
assert(min_num_jumps(1,4, 2) == 2)
print(min_num_jumps(1,1000000000, 2))
assert(min_num_jumps(1,1000000000, 2) == 500000000)
print(min_num_jumps(1,1000000000, 10))
assert(min_num_jumps(1,1000000000, 10) == 100000000)
print(min_num_jumps(10,85, 30))
assert(min_num_jumps(10,85, 30) == 3)
