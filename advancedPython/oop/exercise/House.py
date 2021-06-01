class House:
    layout = 'square'
    def paint(self, color):
        self.color = color

if __name__ == "__main__":
    # As before, we can access attributes.
    print(House.layout)  # 'square'
    print(House.paint)  # <function House.paint(self, color)>

    # This is the new syntax! Instantiate a class object to get back an instance object.
    home = House()  # `home` is now a _specific_ instance object of type `House`
    print(home)  # <House at 0x....>
    print(type(home) is House)  # True

    home.size = '1000'
    print(home.size)  # 1000
    print(home.__dict__)  # {'size': '1000'}

    home.color = 'red'
    print(home.__dict__)  # {'size': '1000', 'color': 'red'}

    home.num_bathrooms = 2
    home.num_bedrooms = 3
    print(home.__dict__)  # {'size': '1000', 'color': 'red', 'num_bathrooms': 2, 'num_bedrooms': 3}

    home.color = 'blue'
    print(home.color)  # blue
    print(home.num_bathrooms)  # 2