required = 1000000
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

primes = list(reversed(sorted(set(sieve(required)))))
smaller_list = list(reversed(primes))#again soja
perm_primes = primes

fl = primes[0]
for i in xrange(1, len(primes), 1):
	if primes[i] + fl > required:
		smaller_list.pop()
		fl = primes[i]


max_list = []
primes = list(reversed(smaller_list))

for i in xrange(len(primes)):
	for j in xrange(len(primes), i, -1):
		s = sum(primes[i:j])
		l = primes[i:j]
		if s < required:
			if len(l) > len(max_list) and s in perm_primes:
				max_list = l
		else:
			break				

print max_list, sum(max_list), len(max_list)




















