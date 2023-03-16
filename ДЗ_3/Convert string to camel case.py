def to_camel_case(text):
    #https://www.codewars.com/kata/517abf86da9663f1d2000003
    p_1 = 0
    p_2 = 1
    answer = ""

    while p_1 < len(text):

        if text[p_1] == "-" or text[p_1] == "_":
            answer += text[p_2].upper()
            p_1 += 1
            p_2 += 1

        else:
            answer += text[p_1]

        p_1 += 1
        p_2 += 1

    return answer