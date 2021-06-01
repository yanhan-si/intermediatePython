class Cat():
    def __init__(self, name, age, isIndoor=True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        print(f'{self.name} says, "purrrrrr"')

    def __repr__(self):
        return self.name

class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print(f'{self.name} says, "woof!"')

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    herbert = Cat('Herbert', 2)
    herbert.speak()

    rex = Dog('Rex', 2, 'Terrior')
    rex.speak()