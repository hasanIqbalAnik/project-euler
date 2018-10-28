from math import floor, sqrt
try: 
    long
except NameError: 
    long = int

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def count_divisors(lstOfdivs):
	num_divisors = 1
	setOfDivs = set(lstOfdivs)
	for item in setOfDivs:
		n = lstOfdivs.count(item)
		num_divisors *= (n+1)
	return num_divisors

num_triangular = 1
num_natural = 1
incr = 1
first_triangular = num_natural

while(True):
	next_num = num_natural + incr
	next_triangular = first_triangular + next_num
	if(count_divisors(fac(next_triangular)) >= 500):
		print next_triangular
		break
	num_natural = next_num
	first_triangular = next_triangular

