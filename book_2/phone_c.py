def isTWP(str):
    if len(str) !=11:
        return False
    for i in range(0,11):
        if i==4:
            if str[4] !='-':
                return False
        else:
            if str[i].isdecimal()==False:
                return False
    return True
print("0937-123456 是台灣手機號碼: ",isTWP('0937-123456'))
print("02-12345678 是台灣手機號碼: ",isTWP('02-12345678'))