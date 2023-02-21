def eval_object(v):
	#https://www.codewars.com//kata/55c933c115a8c426ac000082
    match v['operation']:
        case "+":
            return v['a'] + v['b']
        case "-":
            return v['a'] - v['b']
        case "/":
            return v['a'] / v['b']
        case "*":
            return v['a'] * v['b']
        case "%":
            return v['a'] % v['b']
        case "**":
            return v['a'] ** v['b']
        case _:
            return 1