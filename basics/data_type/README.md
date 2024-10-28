
# Python Complete Cheat Sheet

## 1. Variables & Data Types
```python
# Assigning Variables
x = 5          # integer
y = 2.5        # float
name = "John"  # string
is_valid = True  # boolean

# Checking types
type(x)  # <class 'int'>
type(y)  # <class 'float'>
```

## 2. Basic Operations
```python
# Arithmetic Operators
a + b    # Addition
a - b    # Subtraction
a * b    # Multiplication
a / b    # Division (float)
a // b   # Division (integer)
a % b    # Modulus
a ** b   # Exponentiation

# Comparisons
a == b   # Equal to
a != b   # Not equal to
a > b    # Greater than
a < b    # Less than
a >= b   # Greater than or equal to
a <= b   # Less than or equal to
```

## 3. Strings
```python
# String Methods
s = "hello world"
s.upper()      # "HELLO WORLD"
s.lower()      # "hello world"
s.replace("hello", "hi")  # "hi world"
s.split()      # ['hello', 'world']

# String Formatting
name = "John"
age = 25
f"Hello, my name is {name} and I am {age} years old."  
# "Hello, my name is John and I am 25 years old."
```

## 4. Lists
```python
# Creating Lists
my_list = [1, 2, 3, "apple", True]

# List Methods
my_list.append(6)     # Adds element to the end
my_list.remove(2)     # Removes element by value
my_list.pop()         # Removes last element
my_list[1]            # Access element at index 1
len(my_list)          # Length of list
```

## 5. Dictionaries
```python
# Creating a Dictionary
my_dict = {"name": "Alice", "age": 25}

# Accessing values
my_dict["name"]        # "Alice"

# Adding/Updating keys
my_dict["job"] = "Engineer"

# Dictionary Methods
my_dict.keys()        # Returns keys
my_dict.values()      # Returns values
my_dict.items()       # Returns key-value pairs
```

## 6. Conditional Statements
```python
if condition:
    # Code block
elif another_condition:
    # Another block
else:
    # Final block
```

## 7. Loops
```python
# For loop
for item in iterable:
    # Code block

# While loop
while condition:
    # Code block
```

## 8. Functions
```python
def my_function(param1, param2):
    return param1 + param2

# Calling a function
my_function(5, 10)
```

## 9. Classes & Objects
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Creating an object
my_dog = Dog("Rex", 5)
my_dog.bark()  # "Woof!"
```

## 10. File Handling
```python
# Reading a file
with open('file.txt', 'r') as file:
    content = file.read()

# Writing to a file
with open('file.txt', 'w') as file:
    file.write("Hello, world!")
```

## 11. Exception Handling
```python
try:
    # Code that may raise an error
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This runs no matter what.")
```

## 12. Modules
```python
# Importing a module
import math
print(math.sqrt(16))  # 4.0
```
