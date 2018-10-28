import math

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


primes = sieve(2000)

def find_prime_factors(n):
    lst = []

    for item in primes:
        if n % item == 0:
            lst.append(item)
    return lst

req_len = 4

d = {}
for i in xrange(209, 1000000):    
    d[i] = find_prime_factors(i)


for i in xrange(209, 1000000):
    if len(d[i]) == len(d[i+1]) == len(d[i+2]) == len(d[i+3]) and len(d[i]) == 4:
        print i, d[i], d[i+1], d[i+2], d[i+3]
