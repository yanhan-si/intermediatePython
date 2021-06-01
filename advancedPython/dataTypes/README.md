### String Formatting

```python
greeting = 'Hello'
group = "wørld"

f"{greeting} {group}!"  # f-strings – interpolate expressions into a string
"{greeting} {group}!".format(greeting=greeting, group=group)  # string-formatting by named groups
"{0} {1}!".format(greeting, group)  # string-formatting by positional groups
"%s %s!" % (greeting, group)  # C-style string-formatting
```

### Multi-line Strings

To print out Multi-line Strings, we use triple quotes.

```python
story =  """Once upon a time there was a very long string that was
            over 100 characters long and could not all fit on the 
            screen at once."""
print(story)
```

It prints the string, but there are a bunch of extra spaces between some of the words

```python
story =  "Once upon a time there was a very long string that was " + \
         "over 100 characters long and could not all fit on the " + \
         "screen at once."
print(story)
```

Still, it is kind of a pain having to type + \ at the end of every line—and it makes our code look a bit messy. It's not too bad, but maybe we could do better.

```python
story =  ("Once upon a time there was a very long string that was "
          "over 100 characters long and could not all fit on the "
          "screen at once.")
print(story)
```

### Escaping Characters

Special characters in string literals can be escaped with the \ character. When escaping single- or double-quotes in text, it's often more convenient to choose the string delimiter that makes your text easy to work with.

```python
print('doesn\'t')  # => doesn't
print("doesn't")   # => doesn't

print('"Yes," he said.')    # => "Yes," he said.
print("\"Yes,\" he said.")  # => "Yes," he said.

print('"Isn\'t," she said.')  # => "Isn't," she said.
```

### Converting Values

The named types `str`, `int`, `float`, and `bool` can be used to convert values from one type to another.

```python
str(42)       # => "42"

int("42")     # => 42
float("2.5")  # => 2.5
float("1")    # => 1.0

int("42.5")   # Raises an error (ValueError).
```

### Truthiness

The conversion of a value to a boolean gives the value an essence of "truthiness" – as a boolean, is this object True or False? Empty objects are "Falsy":

```python
# 'Falsy' values.
bool(None)   # => False
bool(False)  # => False
bool(0)      # => False
bool(0.0)    # => False
bool('')     # => False

# Empty data structures too!
bool([])     # => False
```

