def Sequence3():

    data = int(input())
    count = 0
    for _ in range (data):
        for count in range(1 , data+1):
            print(count+1 , end=" ")
        print()

Sequence3()