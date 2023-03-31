#https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/Rqerjkkkal
N = int(input())
list_ = []
count = 0
for i in range(N):
    list_.append(input())
    if list_[i][0] == 'а' or list_[i][0] == 'б' or list_[i][0] == 'в':
        count += 1
if count == N:
    print("YES")
else:
    print("NO")