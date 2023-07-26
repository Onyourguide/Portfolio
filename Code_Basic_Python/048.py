def sequence7():
    data = int(input())

    for i in range (data):
        for j in range (i+1):
            print(j+1 , end=" ")
        print()

    for i2 in range(data-1):
        for j2 in range (1 , data-i2 ,1):
            print(j2 , end=" ")
        print()
sequence7()
