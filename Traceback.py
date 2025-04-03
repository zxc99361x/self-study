import traceback

def CheckSpeed(speed):
    if speed<70:
        raise Exception("速度太慢了")
    if speed>110:
        raise Exception("速度太快了")

for speed in (60,100,150):
    try:
        CheckSpeed(speed)
    except Exception as e:
        with open("err.txt","a") as f:
            f.write(traceback.format_exc())
            print("錯誤資訊已寫入")
    else:
        print("目前速度: {}".format(speed))
        