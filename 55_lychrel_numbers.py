def is_lychrel(n):
	i = 0
	while(i < 50):
		rev_n = str(n)[::-1]
		n = int(rev_n) + n
		if str(n) != str(n)[::-1]:			
			i += 1
		else:
			return True		
	return False


ctr = 0
for i in xrange(0, 10001, 1):
	if is_lychrel(i) == False:
		ctr += 1
print ctr				

