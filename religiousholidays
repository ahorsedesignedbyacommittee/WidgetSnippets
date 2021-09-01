def easter (y):
    
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    f = (b+8) // 25
    g = (b-f+1) // 3
    h = (19*a+b-d-g+15) % 30
    i = c // 4
    k = c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = (a+11*h+22*l) // 451
    
    month =(h+l-7*m+114) // 31
    day = ((h+l-7*m+114)%31) + 1
        
    return (day, month)
    
    
def passover(y_greg):
    
    #Converting y_greg from Gregorian into Jewish calendar 
    #(This is unambiguous, since 15 Nisan can only be in March or April)
    y = y_greg + 3760
    
    #Calculation in Julian calendar
    a = (12 * y + 17) % 19
    b = y % 4
    total_m = 32 + 4343/98496 + (1 + 272953/492480)*a + b/4 - 313*y/98496
    M = int(total_m)
    m = total_m - M
    c = (3*y + 5*b + M + 5) % 7
    if c in (float(2), float(4), float(6)):
        day = M + 1
    elif c == 1 and a > 6 and m >= 1367/2160:
        day = M + 2
    elif c == 0 and a > 11 and m >= 23269/25920:
        day = M + 1
    else:
        day = M
        
    #Conversion from Julian into Gregorian calendar
    x = y_greg // 100
    day = day + x - 2 - x//4
        
    if day <= 31:
        month = 3
    if day > 31:
        day = day - 31
        month = 4
        
    return (day, month)
