#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/DL6KYE4eaB
n = int(input())
m = int(input())
a = set()
b = set()
for i in range(n + m):
    if (x := input()) in a:
        b.add(x)
    else:
        a.add(x)
c = a ^ b
if len(c) == 0:
    print("Таких нет")
else:
    print(len(c))