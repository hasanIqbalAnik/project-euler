from operator import itemgetter
from collections import defaultdict

sol_dic = defaultdict(lambda : 0)

print sol_dic

ctr = 0
for i in xrange(1000, 1, -1):
	for j in xrange(1, 1000, 1):
		for k in xrange(1, 1000, 1):
			if i + j + k <= 1000:
				if i**2 == j**2 + k**2:
					if i+j+k in sol_dic:
						sol_dic[i+j+k] = sol_dic[i+j+k]+1
					else:
						sol_dic[i+j+k] = 1			
					print i+j+k, i, j, k								



print sorted(sol_dic.items(), key=itemgetter(1))