d = {}
for i in xrange(0,10,1):
	d[i] = pow(i,5) 


lsm = 0
for i in xrange(9, 354294, 1):#354294
	lst = list(str(i))
	dg_sum = sum(d[int(x)] for x in lst)
	if i == dg_sum:
		print i, dg_sum
		lsm += dg_sum

print lsm