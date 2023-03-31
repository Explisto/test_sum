#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/qCXhJgNHI9
m = int(input())
n = int(input())
for i in range(n):
    s = input()
    if len(s) <= m:
        print(s)
    else:
        print(s[:m - 3] + "...")