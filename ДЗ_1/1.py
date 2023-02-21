geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #https://www.codewars.com//kata/57ee4a67108d3fd9eb0000e7
    mark = 0
    birds_no_geese = []
    for i in range(len(birds)):
        for j in range(len(geese)):
            if (birds[i] == geese[j]):
                mark = 1
        if (mark == 0):
            birds_no_geese.append(birds[i])
        j = 0
        mark = 0
    return birds_no_geese