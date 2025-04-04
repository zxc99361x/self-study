class MyException(RuntimeError):
    def __init__(self,arg):
        self.args=arg



def CheckSpeed(speed):
    if speed<70:
        raise Exception("速度太慢了")
    if speed>110:
        raise Exception("速度太快了")
    else:
        raise MyException("快樂駕駛，平安回家")

def convertTuple(tup):
    str=''.join(tup)
    return str

for speed in (60,100,150):
    try:
        CheckSpeed(speed)
    except MyException as e:
        err=convertTuple(e.args)
        print("目前速度: {}，{}".format(speed,err))
    except Exception as e:
        print("現在時速: {}，{}".format(speed,e))