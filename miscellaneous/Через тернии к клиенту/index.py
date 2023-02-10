n = int(input())
id_dict = dict()
sorted_logs = []
sum_time_list = []

for i in range(n):
    inp_list = list(map(str,input().split()))
    days, hours, minutes, id = map(int, inp_list[:4])
    event = inp_list[4]
    if (id not in id_dict):
        id_dict[id] = []
    if (event != 'B'):
        id_dict[id].append(days * 24 * 60 + hours * 60 + minutes)

for key in sorted(id_dict.keys()):
    sum = 0
    dates_in_min = id_dict.get(key)
    dates_in_min.sort()
    for i in range(0, len(dates_in_min), 2):
        sum += dates_in_min[i+1] - dates_in_min[i]
    sum_time_list.append(str(sum))


print(' '.join(sum_time_list))

8
'50 7 25 3632 A'
'14 23 52 212372 S'
'15 0 5 3632 C'
'14 21 30 212372 A'
'50 7 26 3632 C'
'14 21 30 3632 A'
'14 21 40 212372 B'
'14 23 52 3632 B'