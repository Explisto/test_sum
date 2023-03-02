def chess_board(rows, columns):
    #https://www.codewars.com/kata/56242b89689c35449b000059
    ans = []
    line_1 = []
    line_2 = []
    
    for i in range(columns):
        
        if (i % 2 == 0):
            line_1.append("O")

        else:
            line_1.append("X")
    
    i = 0
    
    for i in range(columns):
        
        if (i % 2 == 0):
            line_2.append("X")

        else:
            line_2.append("O")
    
    
    for j in range(rows):
        
        if (j % 2 == 0):
            ans.append(line_1)
        
        else:
            ans.append(line_2)
        
    return ans