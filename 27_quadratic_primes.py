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


b_lst = [x for x in primes if x < 1000]
a_lst = b_lst + [-x for x in b_lst]
#print b_lst

n = 0
cur_max = -9999
for b in b_lst:
	for a in a_lst:
		while(True):
			v = (n**2 + a*n + b) 
			if v in primes:
				n += 1
			else:
				if n > cur_max:
					print 'n is : ', n
					print 'a is: ', a
					print 'b is: ', b
					print '......................................'
					print '......................................'
					cur_max = n
				n = 0
				# print v, ' is not in primes'
				break

print cur_max