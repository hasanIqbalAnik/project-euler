
fact_dic = {}

def fact(n):
	fact_dic[0] = 1
	for i in xrange(1, n+1, 1):
		fact_dic[i] = fact_dic[i - 1] * i			
	return fact_dic			




s = str(fact(100)[100])
print sum([int(x) for x in list(s)])	
