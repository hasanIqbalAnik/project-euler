denoms = sorted([1, 2, 5, 10, 20, 50, 100, 200])
d = [[0 for x in xrange(len(denoms)+1)] for y in xrange(201)]
for i in xrange(1, len(denoms)+1):
	d[0][i] = 1
	
	

def num_ways_of_denoms():
	global d
	global denoms
	for i in xrange(1, 201, 1):
		for j in xrange(1, len(denoms)+1):
			if denoms[j-1] > i: #denoms[j] is the coin, doesn't fit
				print 'it didnt fit',denoms[j-1], i
				d[i][j] = d[i][j-1]
			else: #fits
				d[i][j] = d[i][j-1] + d[i-denoms[j-1]][j]

				

num_ways_of_denoms()
for item in d:
	print item
	print '\n'