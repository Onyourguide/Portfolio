def switch():
    start = int(input())
    count = 0
    for _ in range(1000):
        data = str(input())
        if  data <= 6 :
            count += 1
        if data == "End" :
            return
    print(count)
switch()