class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greet(self):
        print("The name of the person is " , self.name , ". The surname of the person is ", self.surname , "The age of the person is " self.age)

person1 = Greta ("Greta", "Gercari", 17)
person2 = Arianita("Arianita", "Gashi", 22)

print(person1.greet)


