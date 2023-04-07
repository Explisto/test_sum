#https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/UZaLMPWk96
n = int(input())
gold = {}
for i in range(n):
    x, y = map(int, input().strip().split())
    x //= 10
    y //= 10
    if (x, y) in gold.keys():
        gold[(x, y)] += 1
    else:
        gold[(x, y)] = 1
print(max(gold.values()))