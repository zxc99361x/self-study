class Animal():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def __sing(self):
        print(self.__name+str(self.__age),end="歲，很會唱歌，")
    def talk(self):
        self.__sing()
        print("也會模仿人類說話")

bird=Animal("灰鸚鵡",2)
bird.talk()

bird.__age=-1
bird.talk()

#bird.__sing()