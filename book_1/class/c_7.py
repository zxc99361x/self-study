class Animal():
    def fly(self):
        print("時速20公里")
class Bird(Animal):
    def fly(self,speed):
        print("時速"+str(speed)+"公里")
class Plane():
    def fly(self):
        print("時速1000公里")
def fly(speed):
    print("時速"+str(speed)+"英里")

animal=Animal()
animal.fly()

bird=Bird()
bird.fly(60)

plane=Plane()
plane.fly()

fly(5)