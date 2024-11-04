# Python String Datatype - Complete Cheat Sheet

## 1. Creating Strings

```python
# Single and double quotes
s1 = 'Hello'
s2 = "World"

# Triple quotes for multiline strings
s3 = '''This is a
multiline string'''

# String with escape characters
s4 = "He said, \"Python is fun!\""
```

## 2. String Slicing and Indexing

```python
s = "Python"
s[0]     # 'P' (first character)
s[-1]    # 'n' (last character)
s[1:4]   # 'yth' (slice from index 1 to 3)
s[::-1]  # 'nohtyP' (reverse the string)
```

## 3. Common String Methods

```python
s = "hello world"

s.upper()      # "HELLO WORLD"
s.lower()      # "hello world"
s.capitalize() # "Hello world" (capitalizes the first letter)
s.title()      # "Hello World" (capitalizes each word)
s.swapcase()   # "HELLO WORLD" -> "hello world", vice versa
s.replace("world", "Python")  # "hello Python"
```

## 4. Built-in String Functions

```python
# Length of a string
len(s)          # 11

# Check if string contains only alphabetic characters
s.isalpha()     # False (because of space)

# Check if string contains only digits
s.isdigit()     # False

# Check if string is alphanumeric
s.isalnum()     # False (space is not alphanumeric)

# Check if string contains only lowercase or uppercase letters
s.islower()     # True
s.isupper()     # False

# Check if string starts or ends with a substring
s.startswith("he")  # True
s.endswith("ld")    # True

# Find the index of a substring
s.find("world")   # 6 (returns index of first occurrence)
s.rfind("o")      # 7 (finds last occurrence)

# Count occurrences of a substring
s.count("l")      # 3
```

## 5. String Formatting

```python
name = "John"
age = 30

# Using f-strings (Python 3.6+)
f"Hello, my name is {name} and I am {age} years old."

# Using .format() method
"Hello, my name is {} and I am {} years old.".format(name, age)

# Formatting numbers
f"{3.14159:.2f}"  # "3.14" (rounds to 2 decimal places)
```

## 6. String Join, Split, and Strip

```python
# Splitting a string into a list of substrings
s = "apple,banana,orange"
s.split(",")  # ['apple', 'banana', 'orange']

# Joining a list of strings into one
list_of_words = ["Hello", "World"]
" ".join(list_of_words)  # "Hello World"

# Stripping whitespace or characters
s = "   hello   "
s.strip()     # "hello" (removes leading/trailing whitespace)
s.lstrip()    # "hello   " (removes leading whitespace)
s.rstrip()    # "   hello" (removes trailing whitespace)
```

## 7. String Encoding and Decoding

```python
# Encoding to bytes
s = "Hello"
s_bytes = s.encode("utf-8")  # b'Hello'

# Decoding bytes to string
s_decoded = s_bytes.decode("utf-8")  # "Hello"
```

## 8. String Testing Methods

```python
# Check if the string is printable
s.isprintable()  # True

# Check if the string is a valid identifier (e.g., variable name)
s.isidentifier()  # False

# Check if the string contains only whitespace characters
s.isspace()  # False

# Check if the string is a title-cased string
"Hello World".istitle()  # True

# Check if the string is ASCII
s.isascii()  # True (all characters are ASCII)
```

## 9. Escape Characters

```python
\    # Backslash
'    # Single quote
"    # Double quote

    # Newline
	    # Tab
```

## 10. String Comparisons

```python
# Comparison using ==, !=, <, >, etc.
s1 = "abc"
s2 = "ABC"
s1 == s2   # False
s1.lower() == s2.lower()  # True (case-insensitive comparison)
```

## 11. Multiline Strings

```python
# Triple quotes for multi-line strings
multi_line_str = '''This is
a multi-line
string'''
```
