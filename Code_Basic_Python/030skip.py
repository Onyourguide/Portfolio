data1 = int(input())
data2 = int(input())

def vote():
    datamin = data1 - data2 - data2 
    if datamin +2 >= data1  :
        print("Surprising")
    else:
        print("Not surprising")

vote()
