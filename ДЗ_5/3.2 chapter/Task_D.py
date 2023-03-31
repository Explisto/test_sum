#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/AZM9pHPP61
n = int(input())
m = int(input())
a = set()
for i in range(n):
    a.add(input())
b = set()
for i in range(m):
    b.add(input())
c = a & b
if len(c) == 0:
    print("Таких нет")
else:
    print(len(c))