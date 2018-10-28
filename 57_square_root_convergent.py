numer = [1, 3]
denom = [1, 2]
ctr = 0
for i in xrange(2, 1000):
	numer.append(2 * numer[i-1] + numer[i-2])
	denom.append(2 * denom[i-1] + denom[i-2])
	if len(str(numer[i])) > len(str(denom[i])):
		ctr += 1

print ctr		
	
	

	
