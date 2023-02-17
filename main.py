def sum_two_numbers(a,b):
    return a+b

def input_func():
    print("Введите первое число:")
    n_1 = input()
    print("Введите второе число:")
    n_2 = input()
    print("Ответ:")
    print(sum_two_numbers(int(n_1),int(n_2)))

input_func()

