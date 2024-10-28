Here's a Python Object-Oriented Programming (OOP) and Inheritance cheat sheet, covering essential concepts, syntax, and commonly used built-in functions for OOP.

---

# Python OOP and Inheritance Cheat Sheet

## 1. Basic Class Structure

```python
class MyClass:
    # Class attribute (shared by all instances)
    class_attribute = "shared"

    # Constructor (initializer)
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute  # Instance attribute

    # Instance method
    def instance_method(self):
        return f"This is an instance method. Attribute: {self.instance_attribute}"

    # Class method (requires `@classmethod` decorator)
    @classmethod
    def class_method(cls):
        return f"This is a class method. Class attribute: {cls.class_attribute}"

    # Static method (doesn't require access to the instance or class)
    @staticmethod
    def static_method():
        return "This is a static method."
```

## 2. Creating and Using Objects

```python
# Creating an instance of MyClass
obj = MyClass("unique")

# Accessing attributes and methods
print(obj.instance_attribute)        # "unique"
print(obj.instance_method())         # "This is an instance method. Attribute: unique"
print(MyClass.class_method())        # "This is a class method. Class attribute: shared"
print(MyClass.static_method())       # "This is a static method."
```

## 3. Special (Dunder) Methods

Special methods (often called "dunder" methods) allow you to define behaviors for standard operations on objects.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):  # Called by str() and print()
        return f"MyClass with value {self.value}"

    def __repr__(self):  # Called by repr() for official string representation
        return f"MyClass({self.value})"

    def __add__(self, other):  # Called by `+` operator
        return MyClass(self.value + other.value)

    def __len__(self):  # Called by len()
        return len(str(self.value))

# Example usage
obj1 = MyClass(5)
obj2 = MyClass(10)
print(obj1 + obj2)  # Uses __add__ method
print(len(obj1))    # Uses __len__ method
```

## 4. Inheritance

```python
# Base (parent) class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Derived (child) class
class Dog(Animal):
    def speak(self):  # Overrides the speak method of Animal
        return "Woof!"

# Usage
dog = Dog("Buddy")
print(dog.name)      # Inherited attribute
print(dog.speak())   # Overridden method output: "Woof!"
```

## 5. Method Resolution Order (MRO)

The order in which Python looks for methods in a hierarchy is defined by the MRO. You can view it with:

```python
print(Dog.__mro__)
```

## 6. Built-in Functions for OOP

### Common Built-in Functions

```python
# issubclass(child, parent) - Check if a class is derived from another class
print(issubclass(Dog, Animal))  # True

# isinstance(object, class) - Check if an object is an instance of a class (or subclass)
print(isinstance(dog, Animal))  # True

# getattr(object, attribute, default) - Get attribute value, or return default if not found
getattr(dog, "name", "Unknown")  # "Buddy"

# setattr(object, attribute, value) - Set an attribute on an object
setattr(dog, "age", 5)
print(dog.age)  # 5

# delattr(object, attribute) - Delete an attribute from an object
delattr(dog, "age")

# dir(object) - Get a list of attributes and methods of an object
print(dir(dog))

# vars(object) - Get __dict__ attribute of the object (its attributes as a dictionary)
print(vars(dog))

# hasattr(object, attribute) - Check if an object has a given attribute
hasattr(dog, "name")  # True
```

### Built-in Functions for Special Use Cases

```python
# type(object) - Returns the type of an object
print(type(dog))  # <class '__main__.Dog'>

# callable(object) - Check if an object is callable (e.g., a method or function)
callable(dog.speak)  # True

# super() - Used to call a method from the parent class
class Cat(Animal):
    def speak(self):
        # Call the parent class's speak method
        parent_speak = super().speak()
        return f"{parent_speak} Meow!"

cat = Cat("Whiskers")
print(cat.speak())  # "Some sound Meow!"
```

## 7. Encapsulation, Inheritance, and Polymorphism

### Encapsulation

Encapsulation is achieved by controlling access to class attributes with public and private variables.

```python
class MyClass:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def get_private(self):
        return self.__private  # Access private attribute through a method

# Accessing attributes
obj = MyClass()
print(obj.public)       # Accessible
print(obj._protected)   # Accessible (though conventionally protected)
print(obj.get_private())  # Accessing private attribute through a method
```

### Polymorphism

Polymorphism allows functions to use different types of objects interchangeably.

```python
class Bird:
    def speak(self):
        return "Chirp"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Demonstrating polymorphism
animals = [Dog("Buddy"), Bird(), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # Calls the overridden method appropriate to the object type
```

## 8. Abstract Classes and Interfaces

Abstract classes are classes that cannot be instantiated and are used as templates.

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Inherits from ABC
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# animal = Animal()  # Raises TypeError because Animal is abstract
dog = Dog()
print(dog.speak())  # "Woof!"
```

---

This cheat sheet provides an overview of Python’s OOP and inheritance concepts, including encapsulation, polymorphism, and abstract classes, along with useful built-in functions. Let me know if you'd like a downloadable version!
