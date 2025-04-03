class Father():
    #def say(self):
        #print("明天會更好嗎?")
    pass
class Mather():
    def say(self):
        print("尊重、包容、友善")
class Child(Father,Mather):
    pass
child=Child()
child.say()