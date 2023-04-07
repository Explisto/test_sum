#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/DnuaPWomud
stack = input().split()
current = []
i = 0
sign = ''

while len(stack) != 1:
    if stack[i + 1].isdigit() is not True:
        current.append(stack[i])
        del stack[i]
        sign = stack[i]
        del stack[i]
        i -= 1
        current.append(stack[i])

        if sign == '+':
            stack[i] = int(current[1]) + int(current[0])
        elif sign == '-':
            stack[i] = int(current[1]) - int(current[0])
        elif sign == '*':
            stack[i] = int(current[1]) * int(current[0])
        current = []

    else:
        i += 1
        
print(stack[0])