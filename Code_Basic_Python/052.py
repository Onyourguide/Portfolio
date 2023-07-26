def sequence10():
    data = int(input())
    count = 1
    for i in range (data):
        # ซ้ายบน metrix = [data x data]
        for j in range (1 , data+1):
            if j <= count :
                print ("%0.2d" % j , end=" ")
            else :
                print ("%0.2d" % count , end=" ")

        # ขวาบน metrix = [data-1 x data-1]
        for j2 in range (data-1,0,-1):
            if j2 >= count :
                print ("%0.2d" % count , end=" ")
            else :
                print ("%0.2d" % j2 , end=" ")
        print()
        count += 1

    count1 = data
    for i2 in range(data-1):
        # ซ้ายล่าง metrix = [data-1 x data]
        for j3 in range (1,data+1):
            if j3 >= count1 :
                print ("%0.2d" % (count1-1) , end=" ")
            else :
                print ("%0.2d" % (j3) , end=" ")
        # ขวาล่าง metrix = [data-1 x data-1]
        for j4 in range (data-1,0,-1):
            if j4 >= count1 :
                print ("%0.2d" % (count1-1) , end=" ")
            else :
                print ("%0.2d" % j4 , end=" ")
        print()
        count1 -= 1

sequence10()
