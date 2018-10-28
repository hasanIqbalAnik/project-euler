from itertools import combinations

x = [x for x in xrange(1, 101, 1)]
S = 0
c = [comb for comb in combinations(x, 2)]
for item in c:
	S += item[0]*item[1]

print 2*S	