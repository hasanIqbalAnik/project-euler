from __future__ import division

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

primes = sieve(100)

def lowest_terms(numer, denom):
	i = 0
	while(i < len(primes)):
		item = primes[i]
		if numer % item == 0 and denom % item == 0:
			numer = numer / item
			denom = denom / item
		else:
			i += 1			
	return numer, denom


for i in xrange(10, 100, 1):
	for j in xrange(10, 100, 1):
		if '0' not in str(i) and '0' not in str(j) and i!=j and j > i:
			numer_set = [int(x) for x in list(str(i)) if x not in list(str(j))]
			denom_set = [int(x) for x in list(str(j)) if x not in list(str(i))]
			if len(numer_set) == 1 and len(denom_set) == 1:					
				numer = numer_set[0]
				denom = denom_set[0]
				lt = lowest_terms(numer, denom)
				numer = lt[0]
				denom = lt[1]
				if numer / denom == i / j:
					print i, j
					print lowest_terms(i, j) 

					print '.'*10
				
