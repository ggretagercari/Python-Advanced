class Animal:

    def sound(self):
        print("Some generic animal sound")

animal = Animal()
print(animal.sound())


class Dog(Animal):
    def sound(self):
        print("woof!")


