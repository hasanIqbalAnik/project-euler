import numpy as np

#memoize matrix multiplication
#generate nth fibo
#check whether it's even
#add to sum


mat_muls = {}

X = np.matrix([[1,1], [1,0]])
m = X
A = np.matrix([[0],[1]])

mat_muls[0] = X

counter = 0
S = 0

while True:
	i = counter+1
	try:
		mat_muls[i].any()
	except:
		mat_muls[i] = mat_muls[i-1] * m		
		v = mat_muls[i] * A
		if(v[0].item() % 2 == 0):
			S = S + v[0].item()
		if(v[0].item() >= 4000000):
			break
		counter = counter + 1

print S