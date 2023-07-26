def theloserls():
    number = int(input())
    round = number-1
    round2 = round
    if round2 % 2 == 0 :
        print (round)
    elif round2 % 2 == 1 :
        print (round)
    else :
        round = int(round) + 1
        print (round) 

theloserls()
