def name_score(name):
	lst_chars = list(name)
	return sum([ord(x)-64 for x in lst_chars])

#print name_score('"COLIN"'[1:-1])	

f = open('p022_names.txt','r')

arr = []
for line in f:
	arr.append(line)

Sum = 0
counter = 1
for item in sorted(arr[0].split(",")):
	Sum += counter * name_score(item[1:-1])
	counter+=1

print Sum	
