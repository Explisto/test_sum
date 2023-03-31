#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/JnnhhAewGx
n = int(input())
a = set()
for i in range(n):
    for j in input().split():
        a.add(j)
print(*a, sep="\n")