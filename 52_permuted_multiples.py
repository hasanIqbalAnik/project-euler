i = 10
flag = True

while flag:
	sn = list(str(i))
	sn2 = list(str(i*2))
	sn3 = list(str(i*3))
	sn4 = list(str(i*4))
	sn5 = list(str(i*5))
	sn6 = list(str(i*6))
	if i == 125874:
		print sorted(sn)
		print sorted(sn2)
		print sorted(sn3)
		print sorted(sn4)
		


	if sorted(sn) == sorted(sn2) == sorted(sn3) == sorted(sn4) == sorted(sn5) == sorted(sn6):
		print i, i*2, i*3, i*4, i * 5, i*6
		flag = False
	else:
		i += 1		