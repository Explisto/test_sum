#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/R3wYYWsSR8
s = input()
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i], count)
        count = 1
print(s[-1], count)