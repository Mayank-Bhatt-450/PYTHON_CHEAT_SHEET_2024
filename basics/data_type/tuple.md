Here's a Python Tuples cheat sheet, including all built-in functions and methods:

---

# Python Tuples Cheat Sheet

## 1. Creating Tuples

```python
# Basic tuple
my_tuple = (1, 2, 3, "apple", True)

# Tuple with one item (add comma)
single_item_tuple = (1,)

# Empty tuple
empty_tuple = ()

# Tuple without parentheses
my_tuple = 1, 2, 3  # Parentheses are optional
```

## 2. Accessing Elements

```python
# Accessing by index
my_tuple[0]   # First element
my_tuple[-1]  # Last element

# Slicing
my_tuple[1:3]  # Elements from index 1 to 2
my_tuple[:2]   # Elements from start to index 1
my_tuple[2:]   # Elements from index 2 to end
```

## 3. Tuple Unpacking

```python
# Unpacking values into variables
t = (1, 2, 3)
a, b, c = t  # a=1, b=2, c=3

# Using the star operator for remaining elements
t = (1, 2, 3, 4)
a, *b, c = t  # a=1, b=[2, 3], c=4
```

## 4. Basic Tuple Operations

```python
# Concatenation
t1 = (1, 2)
t2 = (3, 4)
combined_tuple = t1 + t2  # (1, 2, 3, 4)

# Repetition
repeated_tuple = t1 * 3  # (1, 2, 1, 2, 1, 2)

# Membership
2 in t1  # True
5 not in t1  # True

# Length
len(my_tuple)  # Number of elements
```

## 5. Built-in Tuple Functions

```python
# Minimum element (works with comparable data types)
min((3, 1, 4, 2))  # 1

# Maximum element
max((3, 1, 4, 2))  # 4

# Sum of elements (numeric tuples only)
sum((1, 2, 3))  # 6

# Sorted tuple (returns a list)
sorted((3, 1, 4, 2))  # [1, 2, 3, 4]

# Get the index of the first occurrence of a value
my_tuple.index("apple")  # Index of "apple" in my_tuple

# Count occurrences of a value
my_tuple.count("apple")  # Number of times "apple" appears
```

## 6. Tuple Methods

```python
# Get index of a value (raises ValueError if not found)
my_tuple.index("apple")

# Count occurrences of a value
my_tuple.count("apple")
```

## 7. Converting Between Tuples and Other Types

```python
# Convert list to tuple
my_list = [1, 2, 3]
tuple_from_list = tuple(my_list)  # (1, 2, 3)

# Convert tuple to list
my_tuple = (1, 2, 3)
list_from_tuple = list(my_tuple)  # [1, 2, 3]
```

## 8. Nesting and Tuple of Tuples

```python
# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))

# Accessing nested elements
nested_tuple[1][1]  # 4
```

## 9. Tuple Immutability

```python
# Tuples are immutable, so they cannot be modified after creation
# The following will raise an error:
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## 10. Advantages of Tuples

- **Immutability**: Tuples cannot be changed, which makes them hashable and usable as dictionary keys.
- **Memory Efficient**: Tuples use less memory and are generally faster than lists.

---

This cheat sheet provides a quick reference for working with tuples in Python, including their creation, operations, and built-in functions. Let me know if you need a downloadable file.
