curr_max = -9999

for i in xrange(1, 100):
	for j in xrange(1, 100):
		lst = [int(x) for x in list(str(i**j))]
		if sum(lst) > curr_max:
			print i, j
			curr_max = sum(lst)

print curr_max 			
