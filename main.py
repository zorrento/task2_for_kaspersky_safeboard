#solution isn't completely right, since it gives a half interval as an answer even if it's only in 2 out of N log entries
#plus it's ugly as hell :D

#решение не полностью верное, т.к. оно возвращает полуинтвервал в качестве ответа в том случае, если он "содержится" \
# в друх строках логов (даже если логов > 2) + код очень страшный и написан на скорую руку

N = int(input())
data = []
lengths = []
for i in range(N):
    lengths.append(int(input()))
    data.append(list(map(int,input().strip().split()))[:lengths[i]])
if N == 1:
    print(lengths[0])
    print(*data[0])
    exit()
data_new = []
for i in range(N):
    temp = []
    for j in range(0, lengths[i], 2):
        start = data[i][j]
        end = data[i][j+1]
        temp.append(list(range(start, end)))
    data_new.append(temp)
res = []
for i in range(N-1):
    for j in range(len(data_new[i])):
        for k in range(len(data_new[i+1])):
            start = 0
            if (len(data_new[i][j]) <= len(data_new[i+1][k])):
                for l in range(len(data_new[i+1][k])):
                    if (data_new[i+1][k][l] == data_new[i][j][0]):
                        start = l
                end = min(len(data_new[i][j]), len(data_new[i+1][k][start: start + len(data_new[i][j])]))
                if(data_new[i][j][0:end] == data_new[i+1][k][start: start + end]):
                    res.append(data_new[i][j][0:end])
            else:
                for l in range(len(data_new[i][j])):
                    if (data_new[i][j][l] == data_new[i+1][k][0]):
                        start = l
                end = min(len(data_new[i+1][k]), len(data_new[i][j][start: start + len(data_new[i+1][k])]))
                if(data_new[i+1][k][0:end] == data_new[i][j][start: start + end]):
                    res.append(data_new[i+1][k][0:end])
if not res:
    res = 0
    print(res)
else:
    res_std = []
    for i in res:
        res_std.append(i[0])
        res_std.append(i[-1]+1)
    print(len(res_std))
    print(' '.join(str(e) for e in res_std))