class Animal():
    def __init__(self,name):
        self.name=name
    def sing(self):
        print(self.name+"，很會唱歌")

bird=Animal("鸚鵡")
print(bird.name)
bird.sing()