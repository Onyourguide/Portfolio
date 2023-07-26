def Taxi():
    distance = int(input())
    time = int(input())
    money = 0
    moneytime = time * 1.5
    moneytime2 = moneytime % 2
    if moneytime2 == 0:
        moneytime2 = moneytime
    else :
        moneytime2 = int(moneytime) - 1

    if distance >= 81 :
        distancekilo = ( distance - 81 )
        money = money +  distancekilo * 8.5
        distance = distance - distancekilo

    if distance >= 61 :
        distancekilo = ( distance - 60 )
        money = money +  distancekilo * 7.5
        distance = distance - distancekilo

    if distance >= 41 :
        distancekilo = ( distance - 40 )
        money = money +  distancekilo * 6.5
        distance = distance - distancekilo

    if distance >= 21 :
        distancekilo = ( distance - 20 )
        money = money +  distancekilo * 6
        distance = distance- distancekilo

    if distance >= 13 :
        distancekilo = ( distance - 12 ) 
        money = money + (distancekilo * 5.5)
        distance = distance - distancekilo

    if distance >= 2 :
        distancekilo = ( distance - 1 )
        money = money + distancekilo * 5
        distance = distance - distancekilo

    if distance >= 1 :
        money += 35

    money2 = money % 2
    if money2 == 0:
        money2 = money
    else :
        money2 = int(money) + 1

    print (money2+moneytime2)
Taxi()
