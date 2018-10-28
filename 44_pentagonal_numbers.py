import math

pen_set = set()

def gen_penta(n):
	for i in xrange(1, n):
		pen_set.add((i*(3*i-1))/2)


req = 10000
gen_penta(req)

lst = sorted(pen_set)

for i in xrange(req-1):
	i1 = lst[i]
	for j in xrange(i+1, req-1):
		i2 = lst[j]

		if (i1 + i2) in pen_set:
			if abs(i1 - i2) in pen_set:
				print abs(i1-i2)

