def sequence8():
    data = int(input())
    for i in range (data):
        print("   " * (data-i) , end=" ")
        for j in range (i+1):
            print("%0.2d" % (j+1) , end=" ")
        print()

sequence8()
