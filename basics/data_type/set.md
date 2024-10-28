Here's a Python Sets cheat sheet, including all built-in functions and methods:

---

# Python Sets Cheat Sheet

## 1. Creating Sets

```python
# Basic set
my_set = {1, 2, 3, "apple", True}

# Empty set (use set(), not {})
empty_set = set()

# Set with unique elements (duplicates are removed)
unique_set = {1, 2, 2, 3}  # {1, 2, 3}
```

## 2. Adding and Removing Elements

```python
# Adding a single element
my_set.add(4)  # Adds 4 to the set

# Adding multiple elements
my_set.update([5, 6])  # Adds 5 and 6

# Removing an element (raises KeyError if not found)
my_set.remove("apple")

# Removing an element safely (no error if not found)
my_set.discard("banana")

# Removing and returning a random element
my_set.pop()  # Removes and returns an arbitrary element

# Clearing all elements
my_set.clear()  # Becomes an empty set
```

## 3. Set Operations

```python
# Union (elements from both sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

# Intersection (common elements)
intersection_set = set1 & set2  # {3}

# Difference (elements in set1 but not in set2)
difference_set = set1 - set2  # {1, 2}

# Symmetric Difference (elements in either set, but not both)
symmetric_diff_set = set1 ^ set2  # {1, 2, 4, 5}
```

## 4. Set Methods

```python
# Adding an element
my_set.add(7)

# Updating with multiple elements
my_set.update([8, 9])

# Removing an element (raises KeyError if not found)
my_set.remove(7)

# Discarding an element (no error if not found)
my_set.discard(8)

# Pop (remove and return a random element)
random_element = my_set.pop()

# Copy the set (shallow copy)
copied_set = my_set.copy()
```

## 5. Set Comparisons

```python
# Subset
set1 = {1, 2}
set2 = {1, 2, 3}
set1.issubset(set2)  # True

# Superset
set2.issuperset(set1)  # True

# Disjoint (no elements in common)
set1.isdisjoint({3, 4})  # True
```

## 6. Built-in Set Functions

```python
# len() - Number of elements
len(my_set)  # 5

# max() - Maximum element (only works if elements are comparable)
max({1, 2, 3})  # 3

# min() - Minimum element
min({1, 2, 3})  # 1

# sum() - Sum of elements (only works with numeric sets)
sum({1, 2, 3})  # 6

# sorted() - Sorted list of elements
sorted({3, 1, 2})  # [1, 2, 3]
```

## 7. Membership Testing

```python
# Check if element is in set
2 in my_set  # True

# Check if element is not in set
"banana" not in my_set  # True
```

## 8. Set Comprehensions

```python
# Creating a set with comprehension
squared_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

## 9. Frozen Sets

```python
# Immutable set (cannot be modified after creation)
frozen = frozenset([1, 2, 3])
frozen.add(4)  # Raises AttributeError: 'frozenset' object has no attribute 'add'
```

## 10. Set Conversion

```python
# Convert list or tuple to set (removes duplicates)
list_to_set = set([1, 2, 2, 3])  # {1, 2, 3}
```

---

This cheat sheet provides a quick overview of Python sets, including creation, common operations, methods, and functions. Let me know if you’d like a downloadable version!
