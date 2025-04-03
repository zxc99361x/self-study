try:
    a=int(input("輸入第一個整數:"))
    b=int(input("輸入第一個整數:"))
    r=a%b
except(ValueError,ZeroDivisionError) as e:
    print("發生{}  的錯誤".format(e))
else:
    print("r=",r)
