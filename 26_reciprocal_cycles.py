def next_int(rem, div):
    while(rem < div and rem != 0):
        rem *= 10
        # print rem
    return rem


def cycle_list(num, div):
    lst_div = []
    lst_rem = []

    while(True):
        if num < div:
            num = next_int(num, div)
        res = int(num / div)
        rem = num % div

        if rem in lst_rem:
            return lst_div
        else:
            lst_rem.append(rem)
            lst_div.append(res)
            num = rem

cur_max = -9999
max_num = 0
# for i in xrange(1000, 1, -1):
for i in xrange(1, 1000, 1):
    l = cycle_list(1, i)
    if len(l) > cur_max:
        cur_max = len(l)
        max_num = i

print cur_max, max_num
