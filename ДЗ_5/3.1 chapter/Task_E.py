#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/ov6kYV0VMp
s = input()
p = 0
r = len(s) - 1
flag = True
while p < r:
    if s[p] != s[r]:
        flag = False
    p += 1
    r -= 1
if flag:
    print("YES")
else:
    print("NO")