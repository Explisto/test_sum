#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/kqjNcEAgW2
n = int(input())
d = {}
ans = 0
for i in range(n):
    name = input()
    if name in d.keys():
        d[name] += 1
    else:
        d[name] = 1
for j in d.values():
    if j > 1:
        ans += j
print(ans)