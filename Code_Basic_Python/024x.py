#ยังไม่ได้ทำ ทศนิยม 2 ตำแหน่ง "%.2f" % () ใช้กับ list ไม่ได้

AorD = str(input())
data1 = float(input())
data2 = float(input())
data3 = float(input())
datalist = [data1 , data2 , data3]

def PlanA_Z(x):
    if x == "Ascend":
        datalist.sort()
        print(datalist)
    elif x == "Descend":
        datalist.sort(reverse=True)
        print(datalist)

PlanA_Z(AorD)

#ถ้าไม่ใช้ list 

# AorD = str(input())
# data1 = float(input())
# data2 = float(input())
# data3 = float(input())
# datalist = [data1 , data2 , data3]

# def PlanA_Z(x):
#     if x == "Ascend":
#         datalist.sort()
#         print(datalist)

#     elif x == "Descend":
#         datalist.sort(reverse=True)
#         print(datalist)

# PlanA_Z(AorD)