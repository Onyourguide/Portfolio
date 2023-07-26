def sequence9():
    data = int(input())
    for i in range (data):
        print("   " * (data-i) , end=" ")
        for j in range (i+1):
            print("%0.2d" % (j+1) , end=" ")
        for j in range (1,i+1):
            print("%0.2d" % (i-j+1),end=" ")
        print()
sequence9()
