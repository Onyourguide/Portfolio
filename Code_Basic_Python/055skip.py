def cookieclicker():
    Cbuyfarm = int(input())
    Fcookiepersec = int(input())
    Xfinish = int(input())

    cookie = 0
    cookieperclick = 2
    
    if  cookie < Xfinish :
        cookie += cookieperclick
        second = cookieperclick/2 

    if  cookie >= Cbuyfarm :
        cookie -= Cbuyfarm
        cookieperclick += 2
        Fcookiepersec = cookieperclick

    if cookie >= Xfinish :
        print(second)

cookieclicker()
