try:
    a=int(input("輸入第一個整數:"))
    b=int(input("輸入第一個整數:"))
    r=a%b
except(ValueError,ZeroDivisionError):
    print("發生輸入非整數或分母為0的錯誤")
else:
    print("r=",r)
