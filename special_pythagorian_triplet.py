def check_sum(a, b, c):
	if(a+b+c != 1000):
		return False
	else:
		return True

def check_triplet(a, b, c):
	if(pow(c, 2) == pow(a, 2) + pow(b, 2)):
		return True
	else:
		return False

for i in xrange(1, 500, 1):
	for j in xrange(1, 500, 1):
		for k in xrange(1, 500, 1):
			if(check_triplet(i,j,k) and check_sum(i,j,k)):
				print i*j*k
