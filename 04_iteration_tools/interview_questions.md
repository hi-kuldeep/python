# Python Iteration Interview Questions & Answers 🎯

This document contains top interview questions and detailed answers regarding Python's iteration protocol, iterables, iterators, memory behavior, and related mechanics.

---

## ❓ Question 1: What is the fundamental difference between an "Iterable" and an "Iterator"?

### Answer:
* **Iterable**:
  - An object that has an `__iter__()` method (or a `__getitem__()` method) which returns an iterator.
  - Examples: `list`, `tuple`, `dict`, `str`, `set`, `range`.
  - It represents a sequence of data, but it does **not** keep track of the iteration state (i.e., it doesn't know where it is in a loop).
* **Iterator**:
  - An object that has a `__next__()` method which yields the next item in the sequence.
  - It also has an `__iter__()` method that returns `self` (itself).
  - It remembers its current iteration state (index/position).
  - Calling `next(iterator)` on it advances the cursor and returns the next element.

> [!TIP]
> **Analogy**: An **Iterable** is a book (stores the pages/data). An **Iterator** is a bookmark (remembers which page you are currently on).

---

## ❓ Question 2: Explain how a Python `for` loop works under the hood.

### Answer:
When you write:
```python
for item in iterable:
    # do something
```

Python executes it conceptually as:
1. Calls `iter(iterable)` to retrieve an iterator object.
2. Runs an infinite `while` loop.
3. In each iteration, calls `next(iterator)` (which invokes `__next__()` internally).
4. If an element is returned, it executes the loop body.
5. If a `StopIteration` exception is raised, it catches the exception and exits the loop cleanly.

---

## ❓ Question 3: Why does `iter(my_list) is my_list` evaluate to `False`, while `iter(my_file) is my_file` evaluates to `True`?

### Answer:
* **Lists (Containers)**:
  - Calling `iter(list)` creates a **brand new iterator object** in memory (e.g., `<list_iterator>`). 
  - Each loop or call to `iter(list)` gets its own independent iterator, keeping their pointers separate. This allows multiple concurrent or nested iterations over the same list.
  - Because it is a new object, their memory addresses differ (`iter(list) is list` is `False`).
* **Files (Streams)**:
  - A file object maintains a single file cursor managed by the Operating System.
  - Because the file stream itself acts as the iterator and keeps track of the cursor, calling `iter(file)` returns **the file object itself** (`self`).
  - Thus, they refer to the exact same memory address (`iter(file) is file` is `True`).

---

## ❓ Question 4: When reading a file line-by-line, what is the difference between calling `file.readline()` and `next(file)` / `file.__next__()`?

### Answer:
* **`file.readline()`**:
  - When the end of the file is reached, it returns an empty string (`''`) and continues to return an empty string on subsequent calls. It does **not** raise an exception.
* **`next(file)` or `file.__next__()`**:
  - When the end of the file is reached, it raises a **`StopIteration`** exception. This is crucial because it allows iteration tools (like `for` loops) to know exactly when to terminate.

---

## ❓ Question 5: How can you build a custom iterable class in Python?

### Answer:
To make a class iterable and act as an iterator, you must implement the **Iterator Protocol**:
1. **`__iter__()`**: Returns the iterator object itself (usually `self`).
2. **`__next__()`**: Returns the next item. If no items are left, it must raise a `StopIteration` exception.

#### Example:
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Usage
for num in Counter(3):
    print(num) # Prints 0, 1, 2
```

---

## ❓ Question 6: What is a generator, and how does it relate to iterators?

### Answer:
* A **generator** is a simple and elegant way to create an iterator using a function with the `yield` keyword (instead of `return`).
* When a generator function is called, it returns a **generator object** (which is a subclass of iterator) without executing the function body immediately.
* When `next()` is called on the generator, it runs the function code until it hits a `yield` statement, pauses there, saves its state, and returns the yielded value.
* On subsequent `next()` calls, it resumes right where it left off.
* Generators are memory-efficient because they produce items one by one on-demand (lazy evaluation) rather than storing the whole collection in memory.
