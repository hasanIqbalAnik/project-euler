fibo_dic = {}

fibo_dic[0] = 0
fibo_dic[1] = 1
fibo_dic[2] = 1

def nth_fibo(n):
	if(n in [0, 1, 2]):
		return fibo_dic[n]
	else:
		for i in xrange(3, n+1, 1):
			fibo_dic[i] = fibo_dic[i-1] + fibo_dic[i-2]
	return fibo_dic[n]

counter = 0
while (True):
	l  = len(str(nth_fibo(counter)))
	if(l >= 1000):
		print str(nth_fibo(counter))
		print counter
		break
	else:
		counter += 1



