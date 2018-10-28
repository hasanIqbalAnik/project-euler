#[2, 5, 3, 8, 9, 10, 1, 2, 5, 100]
def max_frm_lst(lst):
	if len(lst) < 4:
		return -1
	else:
		cur_max = -99999
		for i in xrange(len(lst)-3):
			p = lst[i]*lst[i+1]*lst[i+2]*lst[i+3]
			if p > cur_max:
				cur_max = p
				print lst[i], lst[i+1], lst[i+2], lst[i+3]
	return cur_max

l = []
col_list = [[] for i in range(20)]
d1 = [[] for i in range(20)]
d2 = [[] for i in range(20)]
d3 = [[] for i in range(20)]
d4 = [[] for i in range(20)]

with open('p11_nums.txt', 'r') as f: 
	for line in f.readlines():
		l.append([int(x) for x in line.strip().split(" ")])


for i in xrange(20):
	for j in xrange(20):
		col_list[i].append(l[j][i]) 



for i in xrange(20):
	strt = [j for j in xrange(i+1)]
	rev = list(reversed(strt))
	for k in xrange(len(strt)):
		d1[i].append(l[strt[k]][rev[k]]) 

for i in xrange(19, -1, -1):
	strt = [x for x in xrange(20-i)]
	rev = list(reversed(strt))
	for k in xrange(len(strt)):
		d2[i].append(l[19-rev[k]][19-strt[k]])



for i in xrange(19, -1, -1):
	strt = [x for x in xrange(20-i)]
	for item in strt:
		d3[i].append(l[item+i][item])



for i in xrange(19, -1, -1):
	strt = [x for x in xrange(20-i)]
	for item in strt:
		d4[i].append(l[item][item+i])


#print max_frm_lst([2, 5, 3, 8, 9, 10, 1, 2, 5, 100])

cm = -9999
for item in d4:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m

for item in d3:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m
for item in d2:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m
for item in d1:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m
for item in l:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m
	
for item in col_list:
	m = max_frm_lst(item)  
	if m > cm:
		cm = m
print cm