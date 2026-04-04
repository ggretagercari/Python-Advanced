from  abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height


@property
def weight(self):
    return self._weight

@weight.setter
def weight(self, value):
    if value > 0:
        self._weight = value
    else:
        raise ValueError("Weight must be positive")

@property
def height(self):
    return self._height

@height.setter
def height(self, value):
    if value > 0:
        self._height = value
    else:
        raise ValueError("Height must be positive")

@abstractmethod
def calculate_bmi(self):
    pass

@abstractmethod
def get_bmi_category(self):
    pass

def print_info(self):
    bmi = self.calculate_bmi()
    category = self.get_bmi_category()
    print(f"Name: {self.name}, Age: {self.age}, BMI: {bmi:.2f}, Category: {category}")



class Adult(Person):
    def __init__(self, name, age, weight,height):
        super().__init__(name, age, weight, height)

def get_bmi_category(self):
    bmi = self.calculate_bmi()
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"



class Child(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)


def get_bmi_category(self):
    bmi = get_bmi_category()
    if bmi < 14:
        return "Underweight"
    elif bmi < 18:
        return "Normal weight"
    elif bmi < 24:
        return "Overweight"
    else:
        return "Obese"



class BMIApp:
    def __init__(self):
        self.people = []

def add_person(self, person):
    self.people.append(person)

def collect_user_data(self):
    while True:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    self.add_person(person)

while True:
    cont = input("Add another person? (yes/no): ").lower()
    if cont != "yes":9
        break

def print_results(self):
    print("\n--- BMI Results ---")
    for person in self.people:
        person.print_info()



if __name__ == "__main__":
    app = BMIApp()
    app.collect_user_data()
    app.print_results()
