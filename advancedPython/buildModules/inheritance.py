class Animal():
    def __init__(self, name:str, age:int):
        """Create a new cat"""
        self.name = name
        self.age = age

    def speak(self):
        pass

class Cat(Animal):
    isIndoor = True

    def __init__(self, name: str, age:int, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')


class Frog(Animal):

    def __init__(self, name: str, age:int, color='Green'):
        self.color = color
        super().__init__(name, age)


class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')


if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    wiskers.speak()

    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    paws.speak()

    hops = Frog('Hops', 1, 'Blue')
    hops.speak()