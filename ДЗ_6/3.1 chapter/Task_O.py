#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/cXCfPpVk3a
from math import gcd

list_ = [int(x) for x in input().split()]
print(gcd(*list_))