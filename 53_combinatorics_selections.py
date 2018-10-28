com_dic = {}
fact_dic = {}

def fact(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n * fact(n-1)





count = 0

for n in xrange(100, 0, -1):
	for r in xrange(1, n+1, 1):
		numer = 1
		for j in xrange(0, r):
			# print n, r, j
		 	numer = numer * (n - j)
		t =numer / fact(r) 			
		# print t, '...............'
		if t > 1000000:
			count += 1
			print t

print count			


