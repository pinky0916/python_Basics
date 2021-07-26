class Duck:
    def sound(self):
        print("Bow BOW")
class Cow:
    def sound(self):
        print("BAEY BAEY")
class Cat:
    def sound(self):
        print("MEAW MEOW")

def all_sounds(obj):
    obj.sound()
x=Cat()
all_sounds(x)
