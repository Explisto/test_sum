#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/xN8A0sVDQd
s = input()
while s != "":
    if s[0] == "#":
        pass
    elif "#" in s:
        print(s[:s.find("#")])
    else:
        print(s)
    s = input()