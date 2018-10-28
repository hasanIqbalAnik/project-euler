for i in xrange(10000):
	s = str(i*i)
	if s.endswith('0'):
		print i, s
	