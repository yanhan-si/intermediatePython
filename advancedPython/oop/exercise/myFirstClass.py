class MyFirstClass:
    """A simple example class."""
    num = 12345
    def greet(self):
        return "Hello, world"



if __name__ == "__main__":
    print(MyFirstClass.__dict__) # something that acts a lot like a normal dictionary
    print('num' in MyFirstClass.__dict__)  # True
    print('greet' in MyFirstClass.__dict__)
    print(MyFirstClass.num)