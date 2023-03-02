# Create a function args_count, that returns count of passed arguments
def args_count(*args,**kwargs):
    
    #https://www.codewars.com//kata/5c44b0b200ce187106452139
    count = 0
    
    for i in range(len(args)):
        count+=1
 
    for k, v in kwargs.items():
        count+=1
    
    return count