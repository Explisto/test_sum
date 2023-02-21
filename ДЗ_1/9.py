def add(num1, num2):
    #https://www.codewars.com//kata/5effa412233ac3002a9e471d
    a = str(num1)
    b = str(num2)
    c = 0
    ans = ""
    if (len(a)>len(b)):
        count = len(b)
        while (count != len(a)):
            b = "0" + b
            count+=1
            
    if (len(a)<len(b)):
        count = len(a)
        while (count != len(b)):
            a = "0" + a
            count+=1
            
    count = 0
    
    while (count < len(a)):
        c = int(a[count]) + int(b[count])
        ans = ans + str(c)
        count+=1
    return int(ans)
        
        