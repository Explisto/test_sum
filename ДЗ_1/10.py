def find_digit(num, nth):
    #https://www.codewars.com//kata/577b9960df78c19bca00007e
    num = abs(num)
    if (nth > 0):
        s_num = str(num)
        if (nth > len(s_num)):
            return 0
        else:
            return int(s_num[-nth])
    else:
        return -1