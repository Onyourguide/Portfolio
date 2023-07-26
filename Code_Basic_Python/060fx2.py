def blackjack():
    numb = int(input())
    card1 = checkInput(input(), 0)
    card2 = checkInput(input(), card1)
    card3 = 0
    if numb == 3:
        card3 = checkInput(input(), card1+card2)
    print(card1 + card2 + card3)

def checkInput(i, check):
    num = 0
    if i == "A":
        if check + 11 < 21:
            num = 11
        else:
            num = 1
    elif i == "K" or i == "Q" or i == "J":
        num = 10
    else:
        num = i
    return int(num)

blackjack()
