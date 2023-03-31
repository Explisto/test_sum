#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/pKCFLSCyj7
n = int(input())
list_ = []
for i in range(n):
    list_.append(input())
find_ = input()
for j in list_:
    if find_.lower() in j.lower():
        print(j)