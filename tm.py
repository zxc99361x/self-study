try:
    a=int(input("輸入第一個整數:"))
    b=int(input("輸入第一個整數:"))
    r=a%b
    print("r=",r)
except ValueError:
    print("錯誤，輸入非整數")
except Exception as e:
    print("發生",e,"的錯誤，包含分母為0")
finally:
    print("一定會執行區塊")
