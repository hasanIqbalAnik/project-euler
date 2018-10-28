def is_truncatable_prime(p):
    i = 1
    while p % (10**i) != p:
        if p % 10**i not in primes or p / 10**i not in primes:
            return False 
        i+=1
    return True        




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

primes = sieve(1000000)
bad = ['2', '4', '6', '8']
xs = [2, 3, 5, 7]

primes_wo_two = [x for x in primes if set(list(str(x))) & set(bad) == set([])]
pr = [x for x in primes if x not in xs]
print pr
print len(primes_wo_two)
print len(primes)
ctr = 0
S = 0
for item in pr:
    if is_truncatable_prime(item):
        S+= item
        ctr += 1

print ctr        
print S
