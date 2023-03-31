#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/a4hvWnzaSa
n = int(input())
count = 0
for i in range(n):
    str = input()
    count += str.count('зайка')
print(count)