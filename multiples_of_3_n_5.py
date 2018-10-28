S = 0
for i in xrange(1000):
	if( i % 3 == 0 and i % 5 == 0):
		S = S + i
	elif(i % 3 == 0):
		S = S + i
	elif(i % 5 == 0):
		S  = S + i
print S		
