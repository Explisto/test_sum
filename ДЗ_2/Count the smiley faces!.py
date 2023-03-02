def count_smileys(arr):
    #https://www.codewars.com//kata/583203e6eb35d7980400002a
    str = ""
    print(arr)
    count = 0
    n = 0
    flag_1 = False
    flag_2 = False
    flag_3 = False
    
    for i in range(len(arr)):
        
        arr[i].strip()
        a = arr[i].find(":")
        b = arr[i].find(";")
        c = arr[i].find("-")
        d = arr[i].find("~")
        e = arr[i].find(")")
        f = arr[i].find("D")
        g =  arr[i].find("o")
        
        if ((a ==0) or (b == 0)):
            flag_1 = True
        
        if ((c ==1) or (d == 1)):
            flag_2 = True
        
        if ((e ==1) or (f == 1) or (e == 2) or (f == 2)):
            flag_3 = True
        
        if ((flag_1) and (flag_3) == True):
            
            if (g == -1):
                n+=1
            
            print(arr[i])
        
        
        flag_1 = False
        flag_2 = False
        flag_3 = False
            
    return n