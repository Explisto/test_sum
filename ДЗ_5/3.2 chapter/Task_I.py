#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/Tvk8oartND
a = {}
while (inp := input()) != "":
    for i in inp.split():
        a[i] = a.get(i, 0) + 1
for j in a.items():
    print(j[0], j[1])