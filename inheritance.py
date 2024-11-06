#parent class
class Animal():
    def move(self):
        print("Animal is walking...")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

a = Animal()
d = Dog()
d.move()

d.bark()