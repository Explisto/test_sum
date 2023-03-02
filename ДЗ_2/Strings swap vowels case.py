def swap_vowel_case(st): 
    #https://www.codewars.com//kata/5803c0c6ab6c20a06f000026
    
    st_new = ""

    for count in range(len(st)):
        
        if st[count] in "aeiouAEIOU":
            
            if st[count] in "aeiou":
                st_new = st_new + st[count].upper()
            
            if st[count] in "AEIOU":
                st_new = st_new + st[count].lower()
            
        else:
            st_new = st_new + st[count]

        
    return st_new
            