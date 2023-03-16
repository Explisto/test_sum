def unique_in_order(sequence):
    #https://www.codewars.com/kata/54e6533c92449cc251001667
    s = sequence
    p1 = 0
    ans = []
    
    for p2 in range(1,len(s),1):
        
        if s[p1] != s[p2]:
            ans.append(s[p1])
            p1 = p2
    
    if len(s) != 0:
        ans.append(s[-1])
    
    return ans