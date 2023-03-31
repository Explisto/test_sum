#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/OgIDCS3i0M
s = input()
while s != "":
    if s[-3:] == "@@@":
        pass
    elif s[:2] == "##":
        print(s[2:])
    else:
        print(s)
    s = input()