#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/YOO7ZFJH4A
n = int(input())
list_ = [int(input()) for i in range(n)]
step = int(input())
print(*[x ** step for x in list_], sep="\n")