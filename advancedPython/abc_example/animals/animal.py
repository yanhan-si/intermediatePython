from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, age: int):
        """Create a new cat"""
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass
