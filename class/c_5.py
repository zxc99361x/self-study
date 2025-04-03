class Animal():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(self.name+"很會飛")
class Bird(Animal):
    def __init__(self,name):
        self.name="粉紅色"+name
    def sing(self):
        print(self.name+"也愛唱歌")
pigeon=Animal("小白鴿")
pigeon.fly()

parrot=Bird("小鸚鵡")
parrot.fly()
parrot.sing()