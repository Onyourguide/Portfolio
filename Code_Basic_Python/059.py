def Donut():
    bath = int(input())
    amount = int(input())
    free = int(input())
    minimum = int(input())

    if amount + free >= minimum :
        print(bath*amount, amount+free)
    else :
        for i in range (2 , minimum):
            if (amount + free) * i >= minimum:
                break 
            print(bath * amount * i, (amount + free) * 2)

Donut()
