tri_set = set()

def gen_triangular(n):
	for i in xrange(1, n):
		tri_set.add((i*(i+1))/2)

def tri_frm_wrd(word):
	sm = 0
	for item in list(word):
		sm += ord(item) - 64
	return sm		

#gen_triangular(11)


f = open('42.txt', 'r')

word_lst = []
max_len = -9999
for line in f.readlines():
	#word_lst.append(line.split(","))
	word_lst = [x[1:-1] for x in line.split(",")]

for item in word_lst:
	if len(item) > max_len:
		max_len = len(item)

		



gen_triangular(max_len*26 + 1)

count = 0
for item in word_lst:
	if tri_frm_wrd(item) in tri_set:
		count += 1


print count

