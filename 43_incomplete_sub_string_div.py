import itertools
import random
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = [2, 3, 5, 7, 11, 13, 17]
remaining = []
S = 0
perms = itertools.permutations(list(digits), 10)

for item in perms:
	num = int(''.join(map(str, item)))
	if item[3] in [0, 2, 4,6, 8]: #divisible by 2
		if sum(item[2:5]) % 3 == 0: #divisible by 3
			if item[5] == 0 or item[5] == 5: #divisible by 5
				if int(''.join(map(str, item[4:7]))) % 7 == 0: #divisible by 7
					if int(''.join(map(str, item[5:8]))) % 11 == 0:
						if int(''.join(map(str, item[6:9]))) % 13 == 0:
							if int(''.join(map(str, item[7:10]))) % 17 == 0:
								print item
								S += num
								






print S