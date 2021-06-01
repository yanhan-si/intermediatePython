### Code Style

`pycodestyle` is a python tool that checks a given Python script for PEP style violations.

To install `pycodestyle`

```
pip install pycodestyle
```

Then, to run pycodestyle, use this command:

```commandline
pycodestyle bad_style.py
```

[Garbage collection in Python](https://rushter.com/blog/python-garbage-collector/)

[Class Diagrams in UML](https://medium.com/@smagid_allThings/uml-class-diagrams-tutorial-step-by-step-520fd83b300b)

[Deep Copy and Shallow Copy in Python](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

### Exceptions

```python
import re

def validate_email(email):
    """ Test if an email is of a valid format """

    if type(email) is not str:
        raise Exception('Email is not a String')

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex,email):
        raise Exception('Email is Malformed')

    return True
```

### Docstrings

They can be one-liners for obvious cases:

```python
def add(a, b):
     """ Returns the sum of a and b """
    return a + b
```
Or they can be multi-liners for more complex cases:

```python
def divide(a=1, b=2):
     """ Returns the quotient of a divided by b
    Arguments:
        a {int} -- the numerator (defaults 1)
        b {int} -- the denominator (defaults 2)
    Raises:
        Exception: if b is 0
    """
    if b == 0:
       raise Exception("Cannot divide by zero")
    return a / b
```

### Doctest

Doctest is a simple module that allows you to declare expected outputs for specific inputs of a method directly in a docstring comment. For example:

```python
def add(a, b):
    """Return the sum of a and b

    >>> add(1, 1)
    2
    """

return a+b
```