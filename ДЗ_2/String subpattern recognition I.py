def has_subpattern(string):
    #https://www.codewars.com//kata/5a49f074b3bfa89b4c00002b
    count = 0
    mul = 0
    a = ""
    
    while (count <= len(string)):
        a = a + string[count]
        
        mul = len(string) // len(a)
        
        if ((a * mul == string) and (a != string)):
            return True
        
	if (a == string):
            break
        
        count += 1

    return False