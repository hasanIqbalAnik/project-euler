fact_dic = {}

def fact(n):
	if n < 0:
		return
	elif n == 0:
		return 1		
	else:
		fact_dic[0] = 1
		for i in xrange(1, n+1):
			fact_dic[i] = fact_dic[i-1] * i

fact(9)
GS = 0
for i in xrange(10, 999999):
	num_lst = [int(x) for x in list(str(i))]
	S = 0
	for item in num_lst:
		S += fact_dic[item]

	if S == i:
		GS += S


print GS		
