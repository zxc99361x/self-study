class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Triangle(Rectangle):
    def area2(self):
        return (self.width*self.height)/2
        
triangle=Triangle(5,6)
print("矩形面積=",triangle.area())
print("三角形面積=",triangle.area2())