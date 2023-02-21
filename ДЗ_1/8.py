def ones_complement(binary_number):
    #https://www.codewars.com//kata/59b11f57f322e5da45000254
    fin_num = ""
    for count in range(len(binary_number)):
        if (binary_number[count] == "0"):
            fin_num = fin_num + "1"
        else:
            fin_num = fin_num + "0"
    return fin_num
            