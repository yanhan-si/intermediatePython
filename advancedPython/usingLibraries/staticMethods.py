from abc import ABC, abstractmethod

class ConversionStrategy(ABC):
    @staticmethod
    @abstractmethod
    def convert(x):
        pass

class FahrenheitToCelsiusConverter(ConversionStrategy):
    @staticmethod
    def convert(x):
        return (x-32) * 5 / 9

class CelsiusToFahrenheitConverter(ConversionStrategy):
    @staticmethod
    def convert(x):
        return ( x * 9 / 5 ) + 32

if __name__ == "__main__":
    result = FahrenheitToCelsiusConverter.convert(52)
    print(result)

# We can store our strategy objects in a variable that
# can be used later in the code.

def pick_strategy(unit):
    if unit == 'fahrenheit':
        return FahrenheitToCelsiusConverter
    else:
        return CelsiusToFahrenheitConverter

def smart_convert(temp, unit):
    strategy = pick_strategy(unit)
    result = strategy.convert(32)
    print(result)
