In Python, decorators are a powerful and flexible way to modify the behavior of functions or methods without changing their actual code. They are often used for cross-cutting concerns like logging, access control, memoization, and timing.

### What is a Decorator?

A decorator in Python is a function that takes another function as an argument, adds some functionality, and returns a modified function. This concept is based on **higher-order functions**, which either take a function as an argument, return a function, or both.

Decorators are defined using the `@decorator_name` syntax above the function you want to modify. This syntax is shorthand for calling the decorator function and passing the original function to it.

### Basic Structure of a Decorator

A basic decorator has three main parts:

1. **The decorator function itself**: This takes the target function as an argument.
2. **A wrapper function**: This is defined inside the decorator and wraps the target function, adding the extra behavior.
3. **Returning the wrapper function**: The decorator then returns this wrapper function, which replaces the original function.

### Creating a Basic Decorator

Here’s a simple example that adds logging to any function it decorates:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned {result}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

# Using the decorated function
say_hello("Alice")
```

#### Explanation

- `my_decorator` is a decorator that takes a function `func` as an argument.
- `wrapper` is an inner function that:
  - Logs information before and after the function is called.
  - Calls the original function `func` and captures its result.
  - Returns the result.
- `@my_decorator` applies `my_decorator` to `say_hello`.

### Output

```plaintext
Calling function 'say_hello' with arguments ('Alice',) and keyword arguments {}
'say_hello' returned Hello, Alice!
```

### Using Decorators with Arguments

To create a decorator that accepts arguments, you need an additional layer of function wrapping.

Here’s an example of a decorator that repeats the function call a specified number of times:

```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Using the decorated function
greet("Bob")
```

#### Explanation

- `repeat` is a decorator factory that accepts `num_times` as an argument.
- Inside `repeat`, the `decorator` function is defined, which behaves like a standard decorator.
- `@repeat(3)` will apply `repeat` with `num_times = 3` to `greet`.

### Common Use Cases of Decorators

1. **Logging**: Track when and how often functions are called.
2. **Authentication**: Check user permissions before allowing access to certain functions.
3. **Memoization**: Cache results of expensive function calls for faster performance (like `functools.lru_cache`).
4. **Timing**: Measure and log the time taken by a function to execute.

### Built-in Decorators in Python

- **@staticmethod**: Defines a method that doesn’t need access to instance data (`self`).
- **@classmethod**: Defines a method that has access to the class (`cls`) instead of an instance.
- **@property**: Turns a method into a read-only attribute, commonly used in getter/setter logic.

### Example: Timing Decorator

Here’s a decorator that measures the execution time of a function:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function complete.")

# Using the decorated function
slow_function()
```

### Key Points to Remember

- Decorators are functions that take another function and extend its behavior without modifying it.
- They are widely used in Python to keep code modular and readable.
- Decorators can be applied to functions, methods, and even classes.

Decorators are versatile and can be customized to suit different use cases, making them an essential tool for Python development.




Generators in Python are a type of iterable that allow you to create an iterator in a very efficient way. Instead of returning all the values at once, a generator yields one value at a time, which makes it suitable for working with large datasets or streams of data. This is done using the `yield` statement.

### Key Features of Generators

1. **Lazy Evaluation**: Generators compute their values on the fly and yield them one at a time. This means they don't store the entire sequence in memory, making them memory-efficient.
2. **State Preservation**: When a generator function is paused (after yielding a value), it preserves its state, allowing it to resume from where it left off.
3. **Iterators**: Generators are a special kind of iterator, which means they can be iterated over using a loop or other iterable contexts.

### Creating a Generator

You can create a generator using a generator function, which is defined like a normal function but uses the `yield` statement instead of `return`.

#### Example of a Generator Function

Here’s a simple example of a generator that produces a sequence of Fibonacci numbers:

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  # Yield the current value of a
        a, b = b, a + b  # Update a and b for the next Fibonacci number

# Using the generator
fib_gen = fibonacci(10)

for num in fib_gen:
    print(num)
```

### Explanation of the Example

- **Function Definition**: The `fibonacci` function uses `yield` to produce Fibonacci numbers up to `n`.
- **Yielding Values**: Each time `yield` is encountered, the function's state is saved, and the yielded value is returned to the caller.
- **State Preservation**: When the next value is requested, execution resumes right after the last `yield`.

### Using Generators

You can consume generators in several ways:

1. **For Loops**: You can iterate through the generator using a for loop, which retrieves values one at a time.
2. **Next() Function**: You can manually retrieve the next value using the `next()` function.

#### Example of Using Next()

```python
fib_gen = fibonacci(5)
print(next(fib_gen))  # Output: 0
print(next(fib_gen))  # Output: 1
print(next(fib_gen))  # Output: 1
print(next(fib_gen))  # Output: 2
print(next(fib_gen))  # Output: 3
```

### Generator Expressions

In addition to generator functions, Python also allows you to create generators using generator expressions, which are similar to list comprehensions but use parentheses instead of square brackets.

#### Example of a Generator Expression

```python
squares_gen = (x**2 for x in range(10))

for square in squares_gen:
    print(square)
```

### Advantages of Generators

- **Memory Efficiency**: Since generators yield items one at a time, they are more memory-efficient than lists, especially when dealing with large datasets.
- **Simplicity**: Generators can be simpler and more readable than writing an equivalent class-based iterator.
- **Infinite Sequences**: You can create generators that yield an infinite sequence of values, which can be useful in certain applications (e.g., streaming data).

### Example: Infinite Generator

Here’s an example of an infinite generator that yields even numbers:

```python
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

# Using the infinite generator
even_gen = even_numbers()

for _ in range(5):  # Get the first 5 even numbers
    print(next(even_gen))
```

### Conclusion

Generators are a powerful feature in Python that allows for efficient iteration over potentially large datasets without consuming memory unnecessarily. They are especially useful in situations where you need to work with large streams of data or infinite sequences. Understanding how to use generators effectively can lead to more efficient and cleaner code.
