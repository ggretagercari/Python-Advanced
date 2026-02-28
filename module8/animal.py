from warnings import catch_warnings


class Animal:
    def __init__(self, typeOfAnimal, raca, ngjyra):
        self.typeOFAnimal = typeOfAnimal
        self.raca = raca
        self.ngjyra =  ngjyra

    def greet(self):
        print("The tye of Animal is ", self.typeOFAnimal, ". The race is ", self.raca, ".And the color is ", self.ngjyra)


dog = Animal ("Dog", "Husky", "White")
cat = Animal ("Cat", "British", "Gray")

print(dog.greet())
print(cat.greet())