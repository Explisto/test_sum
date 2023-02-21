def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    #https://www.codewars.com//kata/5b7ea71db90cc0f17c000a5a
    a = (given_mass1/molar_mass1)
    b = (given_mass2/molar_mass2)
    T = temp + 273.15
    R = 0.082
    return ((a+b)*R*T)/(volume)