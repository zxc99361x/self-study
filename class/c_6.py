class Animal():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(self.name+"很會飛")
class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def fly(self):
        print(str(self.age),end="歲")
        super().fly()

pigeon=Animal("小白鴿")
pigeon.fly()

parrot=Bird("小鸚鵡",2)
parrot.fly()