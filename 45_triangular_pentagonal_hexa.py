tri_set = set()
pen_set = set()
hex_set = set()

req = 500000

def gen_triangular(n):
	for i in xrange(1, n):
		tri_set.add((i*(i+1))/2)

def gen_penta(n):
	for i in xrange(1, n):
		pen_set.add((i*(3*i-1))/2)

def gen_hexa(n):
	for i in xrange(1, n):
		hex_set.add((i*(2*i-1)))


gen_triangular(req)
gen_penta(req)
gen_hexa(req)

print tri_set & pen_set & hex_set

#print sorted(tri_set)
#print sorted(pen_set)
#print sorted(hex_set)