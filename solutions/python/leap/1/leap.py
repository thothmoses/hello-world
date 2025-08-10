def leap_year(year):
    fr=False
    hun=False
    four_hun=False
    print(year%4)
    print(year%100)
    print(year%400)
    if year % 4 != 0:
        fr = False
        print(fr)    
    if year % 4 == 0:
        fr = True
        print(fr)
    if year % 100 == 0: 
        hun = True
        print(fr)
    if year % 400 == 0:
        four_hun = True
        print(four_hun)
    if fr == False:
        p = False
    if fr == True and hun == False:
        p = True
    if fr == True and four_hun == True:
        p = True
    if fr == True and hun == True and four_hun == False:
        p = False


    return p

pass
