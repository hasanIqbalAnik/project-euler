def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

primes = sieve(100000)
twice_squares = [2*i*i for i in xrange(1, 1001)]
odd_composite = [x for x in xrange(10000) if x not in primes and x %2 != 0]

def can_be_represented(n):
    for i1 in twice_squares:
        for i2 in primes:
            if item == i1+i2:
                return True
    return False                





for item in odd_composite:
    if can_be_represented(item) == False:
        print item

