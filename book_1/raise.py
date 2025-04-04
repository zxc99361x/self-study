def CheckSpeed(speed):
    if speed<70:
        raise Exception("速度太慢了")
    if speed>110:
        raise Exception("速度太快了")

for speed in (60,100,150):
    try:
        CheckSpeed(speed)
    except Exception as e:
        print("現在速度: {}，{}".format(speed,e))
    else:
        print("目前時速: {}".format(speed))