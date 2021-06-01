class Cat():

    def __init__(self, name: str, age: int):
        if (type(name) is not str):
            raise Exception('Name must be a string')

        if(age < 0):
            raise Exception('Age must be greater than 0')
        self.name = name
        self.age = age

    def speak(self) -> None:
        print(f'{self.name} says, "purrrrrr"')

if __name__ == "__main__":
    try:
        herbert = Cat('herbert', -1)
        herbert.speak()
    except:
        print('Bad Cat')