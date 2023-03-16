def is_rotation(s1,s2):
    #https://www.codewars.com/kata/55467aaf72494e3bdc00007f
    p1 = 0
    p2 = 0
    
    if s1 == s2:
        return True

    if len(s1) != len(s2):
        return False
    
    if s1 == "" and s2 == "":
        return False

    for count in range(len(s1)):

        p1 = count
        p2 = 0

        for str_count in range(len(s1)):

            if s1[p1] == s2[p2]:
                
                if p1 == len(s1) - 1:
                    p1 = 0
                    p2 += 1
                
                else:
                    p1 += 1
                    p2 += 1

        if p2 == len(s1):
            return True

    return False