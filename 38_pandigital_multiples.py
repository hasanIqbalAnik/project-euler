def is_pandigital(n):
	i = 123456789
	
	if len(str(n)) != 9:
		return False
	elif sorted(list(str(n))) != sorted(list(str(i))):
		return False
	else:
		return True

curr_max = -99999

for i in xrange(9999, 1, -1):
	tmp = ''
	for j in xrange(1, 10):
		tmp += str(i * j)
		if len(tmp) > 9:
			break
		elif is_pandigital(int(tmp)) and int(tmp) > curr_max:
			curr_max = int(tmp)
			print curr_max


print curr_max			
