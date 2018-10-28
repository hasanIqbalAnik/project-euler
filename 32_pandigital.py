import itertools


it = (1, 2, 3, 4, 5, 6, 7, 8, 9)


st = []
for item in list(itertools.permutations(it,2)):
	other_except_it = [x for x in it if x not in item]
	#print item
	three_length = list(itertools.permutations(other_except_it, 3))
	for tl_item in three_length:
	#	print tl_item
		others_except_it_except_three = [x for x in other_except_it if x not in tl_item]
	#	print others_except_it_except_three
		for four_len in list(itertools.permutations(others_except_it_except_three, 4)):
			#work with item(len 2), tl_item(len 3) and four_len
			a = int(''.join(str(x) for x in item))
			b = int(''.join(str(x) for x in tl_item)) 
			c = int(''.join(str(x) for x in four_len))
			if (a*b == c and c not in st):
				print a, b, c
				print c
				st.append(c)


for item in list(itertools.permutations(it,3)):
	other_except_it = [x for x in it if x not in item]
	#print item
	three_length = list(itertools.permutations(other_except_it, 3))
	for tl_item in three_length:
	#	print tl_item
		others_except_it_except_three = [x for x in other_except_it if x not in tl_item]
	#	print others_except_it_except_three
		for four_len in list(itertools.permutations(others_except_it_except_three, 3)):
			#work with item(len 2), tl_item(len 3) and four_len
			a = int(''.join(str(x) for x in item))
			b = int(''.join(str(x) for x in tl_item)) 
			c = int(''.join(str(x) for x in four_len))
			if (a*b == c):
				print a, b, c
				print c				
				st.append(c)



for item in list(itertools.permutations(it,1)):
	other_except_it = [x for x in it if x not in item]
	#print item
	three_length = list(itertools.permutations(other_except_it, 4))
	for tl_item in three_length:
	#	print tl_item
		others_except_it_except_three = [x for x in other_except_it if x not in tl_item]
	#	print others_except_it_except_three
		for four_len in list(itertools.permutations(others_except_it_except_three, 4)):
			#work with item(len 2), tl_item(len 3) and four_len
			a = int(''.join(str(x) for x in item))
			b = int(''.join(str(x) for x in tl_item)) 
			c = int(''.join(str(x) for x in four_len))
			if (a*b == c):
				print a, b, c
				print c				
				st.append(c)

print sum(st)