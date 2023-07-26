def sequence10():
    data = int(input())
    for i in range (data): 
        for j in range (data-i,data+1,1):
            print("%0.2d" % j , end=" ")
        for k in range (data-1,i,-1):
            print("%0.2d" % k , end=" ")
        for l in range (2+i,data+1,1):
            print("%0.2d" % (l) , end=" ")
        for m in range (data,data-i,-1):
            print("%0.2d" % (m-1) , end=" ")
        print()

    for i2 in range (data-1):
        for j2 in range (2+i2,data+1,1):
            print("%0.2d" % (j2) , end=" ")
        for k2 in range (data+1,data-i2,-1):
            print("%0.2d" % (k2-2) , end=" ")
        for l2 in range (data-i2,data+1,1):
            print("%0.2d" % (l2) , end=" ")
        for m2 in range (data-1,i2+1,-1):
            print("%0.2d" % (m2) , end=" ")
        print()


    # count1 = data
    # for i2 in range(data-1):
    #     # ซ้ายล่าง metrix = [data-1 x data]
    #     for j3 in range (1,data+1):
    #         if j3 >= count1 :
    #             print ("%0.2d" % (count1-1) , end=" ")
    #         else :
    #             print ("%0.2d" % (j3) , end=" ")
    #     # ขวาล่าง metrix = [data-1 x data-1]
    #     for j4 in range (data-1,0,-1):
    #         if j4 >= count1 :
    #             print ("%0.2d" % (count1-1) , end=" ")
    #         else :
    #             print ("%0.2d" % j4 , end=" ")
    #     print()
    #     count1 -= 1

sequence10()
