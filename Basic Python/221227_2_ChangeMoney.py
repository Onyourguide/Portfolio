#แลกเงิน

a = int(input("Money = "))

if a >= 1000 :
    print("1000 บาท" ,a//1000, "ใบ")
    a = a%1000

if a >= 500 :
    print("500 บาท" ,a//500, "ใบ")
    a = a%500

if a >= 100 :
    print("100 บาท" ,a//100, "ใบ")
    a = a%100

if a >= 50 :
    print("50 บาท" ,a//50, "ใบ")
    a = a%50

if a >= 20 :
    print("20 บาท" ,a//20, "ใบ")
    a = a%20
    
if a >= 1 :
    print("1 บาท" ,a//1, "เหรียญ")
    a = a%1