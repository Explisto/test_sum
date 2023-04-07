#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/8Ymb2732go
n = int(input())
s = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(n):
    print(s[i % 5])