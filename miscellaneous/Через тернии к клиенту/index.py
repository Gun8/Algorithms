n = int(input())
id_dict = dict()
sorted_logs = []
sum_time_list = []

for i in range(n):
    log = list(map(str,input().split()))
    id = int(log[3])
    if (id not in id_dict):
        id_dict[id] = []
    if (log[4] != 'B'):
        id_dict[id].append(int(log[0]) * 24 * 60 + int(log[1]) * 60 + int(log[2]))

for key in sorted(id_dict.keys()):
    sum = 0
    dates_in_min = id_dict.get(key)
    dates_in_min.sort()
    for i in range(0, len(dates_in_min), 2):
        sum += dates_in_min[i+1] - dates_in_min[i]
    sum_time_list.append(str(sum))


print(' '.join(sum_time_list))

