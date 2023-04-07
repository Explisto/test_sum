#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/5vjFLZ1M9w
list_ = [int(x) for x in input().split()]
step = int(input())
print(*[x ** step for x in list_])