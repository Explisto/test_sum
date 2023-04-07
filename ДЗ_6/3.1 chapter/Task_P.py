#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/LGkorFrReo
length = int(input()) - 3
n = int(input())
list_ = [input() for x in range(n)]
for line in list_:
    if length >= len(line):
        length -= len(line)
        if length <= 0:
            print(line + "...")
            break
        else:
            print(line)
    elif list_[-1] == line and length + 3 >= len(line):
        print(line)
    else:
        if length <= 0:
            print("...")
        else:
            print(line[:length] + "...")
        break