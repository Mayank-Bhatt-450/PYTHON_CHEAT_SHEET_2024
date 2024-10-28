
# Python Complete Cheat Sheet (Extended)

## 1. Variables & Data Types
```python
# Common Data Types
x = 5                 # int
y = 2.5               # float
name = "John"         # str
is_valid = True       # bool
my_list = [1, 2, 3]   # list
my_tuple = (1, 2, 3)  # tuple
my_dict = {"key": "value"}  # dict
my_set = {1, 2, 3}    # set

# Type Conversion
int("5")    # 5
str(5)      # "5"
float("2.5")  # 2.5
bool(1)     # True
```

## 2. Built-in Data Types and Functions
```python
# Numeric Types: int, float, complex
a = 10
b = 3.5
c = 1 + 2j  # complex number

# Built-in Functions:
abs(-5)           # Absolute value: 5
round(3.14159, 2) # Rounds to 2 decimal places: 3.14
pow(2, 3)         # Exponentiation: 8
divmod(9, 4)      # Returns (quotient, remainder): (2, 1)
sum([1, 2, 3])    # Sum of elements: 6
min(1, 2, 3)      # Minimum: 1
max(1, 2, 3)      # Maximum: 3
```

## 3. Strings (Additional)
```python
# String Methods (cont.)
s = "hello world"
s.startswith("he")  # True
s.endswith("ld")    # True
s.find("world")     # 6 (returns index of substring)
s.count("l")        # 3

# String Slicing
s = "Python"
s[0:3]   # "Pyt" (from index 0 to 2)
s[::-1]  # "nohtyP" (reverses the string)
```

## 4. Lists (Additional)
```python
# List Comprehensions
squared_numbers = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Sorting Lists
sorted_list = sorted(my_list)  # Returns a sorted list
my_list.sort()  # Sorts the list in place

# Other List Functions
my_list.extend([4, 5])   # Adds multiple elements
my_list.index(3)         # Finds index of value
```

## 5. Tuples
```python
# Tuples are immutable
my_tuple = (1, 2, 3)
single_element_tuple = (1,)  # Note the trailing comma

# Tuple Packing/Unpacking
a, b, c = (1, 2, 3)
```

## 6. Dictionaries (Additional)
```python
# Dictionary Methods (cont.)
my_dict = {"name": "Alice", "age": 25}
my_dict.get("name")  # "Alice" (returns value for key, or None)
my_dict.pop("age")   # Removes key and returns its value
my_dict.update({"job": "Engineer"})  # Merges two dictionaries
```

## 7. Sets
```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Set Methods
my_set.add(6)       # Adds an element
my_set.remove(3)    # Removes an element
my_set.union({6, 7})  # Returns union of two sets
my_set.intersection({4, 5})  # Returns intersection
```

## 8. OOP - Object-Oriented Programming

### Class Definition and Inheritance
```python
# Defining a class with inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a noise."

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        return f"{self.name} barks."

# Creating an object
dog = Dog("Rex")
print(dog.speak())  # "Rex barks"
```

### Interfaces (using Abstract Base Classes)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Creating an object of Circle
circle = Circle(5)
print(circle.area())  # 78.5
```

## 9. Functions (Additional)
```python
# Lambda (Anonymous) Functions
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)  # 120
```

## 10. Built-in Functions (Additional)
```python
# all() - Returns True if all elements in an iterable are true
all([True, True, False])  # False

# any() - Returns True if any element in an iterable is true
any([False, True, False])  # True

# isinstance() - Checks if object is an instance of a class
isinstance(5, int)  # True

# enumerate() - Adds a counter to an iterable
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)  # 0 a, 1 b, 2 c

# zip() - Combines multiple iterables into tuples
list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# eval() - Evaluates a string expression
eval('5 + 5')  # 10
```

## 11. Exception Handling (Additional)
```python
# Raising Exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Custom Exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e)
```

## 12. File Handling (Additional)
```python
# Reading files line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open('file.txt', 'a') as file:
    file.write("This is an appended line.
")
```
