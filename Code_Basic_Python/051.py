def sequence9():
    data = int(input())
    for i in range (data):
        print("   " * (data-i) , end=" ")
        for j in range (i+1):
            print("%0.2d" % (j+1) , end=" ")

        for j in range (1,i+1):
            print("%0.2d" % (i-j+1),end=" ")
        print()
    
    for i2 in range (data-2,-1,-1):
        print("   " * (data-i2) , end=" ")
        for j2 in range (i2+1):
            print("%0.2d" % (j2+1) , end=" ")

        for j2 in range (1,i2+1):
            print("%0.2d" % (i2-j2+1),end=" ")
        print()
sequence9()
