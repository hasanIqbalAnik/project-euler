one_lst = [1]
eighty_nine_lst = [89]
one_ctr = 0

def square_and_add(n):
	global one_lst
	global eighty_nine_lst
	lst = []
	# print '\n', n, '-> ',
	while True:
		n = sum([int(y)**2 for x in list(str(n)) for y in x])
		# print n, ' -> ', 
		if n in one_lst:
			one_lst += lst
			# print ' will end at 1'
			return 1			
		elif n in eighty_nine_lst:
			# print ' will end at 89'
			eighty_nine_lst += lst
			return 0			
		else:
			lst.append(n)				
	if n == 1:
		one_lst+=lst
	else:
		eighty_nine_lst += lst		
	return 1				


for i in xrange(1, 10000000):
	one_ctr += square_and_add(i)

print 9999999 - one_ctr
# print one_lst
# print eighty_nine_lst
	
