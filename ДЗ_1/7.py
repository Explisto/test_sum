def swap_values(args): 
	#https://www.codewars.com//kata/5388f0e00b24c5635e000fc6
    a = args[1]
    args[1] = args[0]
    args[0] = a
    return args