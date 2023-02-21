def difference_in_ages(ages):
    #https://www.codewars.com//kata/5720a1cb65a504fdff0003e2
    max_age = 0
    min_age = 200
    for count in range(len(ages)):
        if (ages[count] > max_age):
            max_age = ages[count]
        if (ages[count] < min_age):
            min_age = ages[count]
    ages_t = (min_age,max_age,max_age-min_age)
    return ages_t