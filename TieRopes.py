__author__ = 'jmasramon'


if __name__ == '__main__':
    print 'Start tests..'
    assert greedyCoinChangeing([1, 2, 5], 6) == [(5, 1), (2, 0), (1, 1)]  # Correct
