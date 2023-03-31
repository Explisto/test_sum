#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/s6Jxtvde9U
n = int(input())
d = {}
ans = []
for i in range(n):
    name = input()
    if name in d.keys():
        d[name] += 1
    else:
        d[name] = 1
for j in d.keys():
    if d[j] > 1:
        ans.append(j)
ans.sort()
if ans:
    for k in ans:
        print(f'{k} - {d[k]}')
else:
    print("Однофамильцев нет")