#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/zto47acz4L
s = input()
k = 0
r = len(s) - 1
while k < r:
    while s[k] == " " and k < r:
        k += 1
    while s[r] == " " and k < r:
        r -= 1
    if s[k].lower() != s[r].lower():
        print("NO")
        break
    k += 1
    r -= 1
else:
    print("YES")