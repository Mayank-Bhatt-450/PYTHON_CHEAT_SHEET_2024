Here's a Python Dictionaries cheat sheet, including all built-in functions and methods:

---

# Python Dictionaries Cheat Sheet

## 1. Creating Dictionaries

```python
# Basic dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Empty dictionary
empty_dict = {}

# Using the dict() constructor
constructed_dict = dict(name="Bob", age=30)

# From a list of tuples
tuple_list = [("name", "Charlie"), ("age", 35)]
dict_from_tuple = dict(tuple_list)
```

## 2. Accessing and Modifying Elements

```python
# Accessing values by key
my_dict["name"]  # "Alice"

# Adding or updating a key-value pair
my_dict["email"] = "alice@example.com"

# Removing a key-value pair (raises KeyError if key not found)
del my_dict["city"]

# Using `pop()` to remove and return a value by key
age = my_dict.pop("age")

# Using `popitem()` to remove and return the last key-value pair
last_item = my_dict.popitem()  # Returns a (key, value) tuple

# Using `get()` to retrieve a value safely (no KeyError if key is missing)
city = my_dict.get("city", "Unknown")  # Returns "Unknown" if "city" not found
```

## 3. Dictionary Methods

```python
# keys() - Returns all keys as a dict_keys object
my_dict.keys()

# values() - Returns all values as a dict_values object
my_dict.values()

# items() - Returns all key-value pairs as a dict_items object
my_dict.items()

# update() - Adds or updates multiple key-value pairs from another dictionary or iterable
my_dict.update({"city": "Los Angeles", "phone": "123-456-7890"})

# clear() - Removes all key-value pairs
my_dict.clear()

# copy() - Creates a shallow copy of the dictionary
dict_copy = my_dict.copy()
```

## 4. Dictionary Comprehensions

```python
# Basic dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## 5. Built-in Dictionary Functions

```python
# len() - Number of key-value pairs
len(my_dict)

# sorted() - Returns a sorted list of dictionary keys
sorted(my_dict)  # Sorted list of keys
```

## 6. Checking for Keys

```python
# Checking if a key exists
"name" in my_dict  # True

# Checking if a key does not exist
"email" not in my_dict  # True
```

## 7. Iterating Through a Dictionary

```python
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

## 8. Nested Dictionaries

```python
# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# Accessing nested values
name = nested_dict["person1"]["name"]
```

## 9. Merging Dictionaries (Python 3.9+)

```python
# Using the | operator to merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}

# Using the |= operator to update a dictionary in place
dict1 |= dict2  # dict1 is now {"a": 1, "b": 3, "c": 4}
```

## 10. Dictionary Conversion

```python
# Convert two lists to a dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dict_from_lists = dict(zip(keys, values))  # {"name": "Alice", "age": 25, "city": "New York"}
```

---

This cheat sheet provides a concise overview of working with dictionaries in Python, including all commonly used functions, methods, and operations. Let me know if you’d like a downloadable version!
