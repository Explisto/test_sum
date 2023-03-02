# you can either create a valid regex to find if a character
# is a JoJo or create a function for it.
# bonus points if you do both ;)

# Oh, and think about beginners: try to be informative and
# comment with some explanation for the sake of their learning!

regex = "" # your regex here or...

def is_jojo(name):
    #https://www.codewars.com//kata/55327e12f5363713200000e4
    flag = False

    name_check = name.strip()

    name_1 = ""

    name_2 = ""

    k = name_check.split()
    
    if (len(k) == 1):
        
        return False
    
    name_1 = k[0]
    
    name_2 = k[1]


    if ((name_1[0:2].lower() == "jo") and (name_2[0:2].lower() == "jo")):
        return True
    

    if ((name_1[0:2].lower() == "jo") and (name_2[-2:].lower() == "jo")):
        return True

    if ((name_1[0:3].lower() == "gio") and (name_2[0:3].lower() == "gio")):
        return True

    return False


        
        
        