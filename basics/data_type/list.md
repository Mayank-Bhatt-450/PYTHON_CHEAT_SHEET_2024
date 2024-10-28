Here’s a Python Lists cheat sheet, including all built-in functions and methods:

---

# Python Lists Cheat Sheet

## 1. Creating Lists

```python
# Basic list
my_list = [1, 2, 3, "apple", True]

# Empty list
empty_list = []

# Lists with different types
mixed_list = [1, "hello", 3.14, False]
```

## 2. Accessing Elements

```python
# By index
my_list[0]  # First element
my_list[-1]  # Last element

# Slicing
my_list[1:3]  # Elements from index 1 to 2
my_list[:2]   # Elements from start to index 1
my_list[2:]   # Elements from index 2 to end
```

## 3. Modifying Lists

```python
# Changing an element
my_list[1] = "banana"

# Adding elements
my_list.append(4)  # Adds 4 at the end
my_list.insert(1, "orange")  # Inserts "orange" at index 1

# Removing elements
my_list.remove("banana")  # Removes the first "banana"
my_list.pop()             # Removes last element
my_list.pop(1)            # Removes element at index 1
del my_list[0]            # Deletes element at index 0

# Clearing list
my_list.clear()  # Removes all elements
```

## 4. List Operations

```python
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4]

# Repetition
repeated = list1 * 3  # [1, 2, 1, 2, 1, 2]

# Membership
2 in list1  # True
5 not in list1  # True

# Length
len(my_list)  # Number of elements
```

## 5. Built-in List Functions

```python
# Minimum element
min([3, 1, 4, 2])  # 1

# Maximum element
max([3, 1, 4, 2])  # 4

# Sum of elements (only for numeric lists)
sum([1, 2, 3])  # 6

# Sorted list (returns new sorted list)
sorted([3, 1, 4, 2])  # [1, 2, 3, 4]

# Reverse iterator
list(reversed([1, 2, 3]))  # [3, 2, 1]
```

## 6. List Methods

```python
# Add an element
my_list.append(5)

# Extend with another list
my_list.extend([6, 7])

# Insert at specific index
my_list.insert(1, "banana")

# Remove first occurrence of a value
my_list.remove("banana")

# Remove and return item at index (default: last)
my_list.pop()

# Get index of first occurrence of a value
my_list.index("apple")

# Count occurrences of a value
my_list.count("apple")

# Sort in place
my_list.sort()

# Reverse in place
my_list.reverse()

# Shallow copy of list
copy_list = my_list.copy()
```

## 7. List Comprehensions

```python
# Basic comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Comprehension with condition
evens = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
```

## 8. List Iteration

```python
# Iterate over elements
for item in my_list:
    print(item)

# Iterate with index
for index, item in enumerate(my_list):
    print(index, item)
```

## 9. Nested Lists

```python
# Nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in nested lists
nested[0][1]  # 2 (second element of the first sublist)
```

## 10. List Copying

```python
# Shallow copy (references to elements)
shallow = my_list.copy()

# Deep copy (copy of elements)
import copy
deep_copy = copy.deepcopy(nested)
```

## 11. Deleting Lists and Elements

```python
# Delete an element by index
del my_list[1]

# Delete the entire list
del my_list
```

## 12. Membership Testing

```python
# Check if element exists
"apple" in my_list  # True

# Check if element does not exist
"banana" not in my_list  # True
```

---

This cheat sheet covers most common methods and operations on lists, making it a handy reference for Python list manipulation! Let me know if you need a downloadable version.
