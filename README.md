# Learning Python 🐍

Welcome to my Python learning repository! This project serves as a step-by-step guide to mastering Python, starting from core mechanics to standard features, iteration protocols, functions, scopes, and hands-on problem sets.

---

## 📚 Study Plan & Repo Structure

Here is the index of all chapters, deep-dive guides, and practice problem sets in this repository:

### 1️⃣ Chapter 01: Python Basics & Data Types
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Python Basics & Inner Workings** | PVM, Compiling to Bytecode, `.pyc` caching in `__pycache__`, Python implementations (CPython, PyPy). | [Go to Basics & Inner Workings 🚀](./01_basics/README.md) |
| **Memory Reference & Mutability** | Variables as pointers, reference sharing, mutable vs immutable types with flow diagrams. | [Go to Memory Reference 🧠](./01_basics/memory_reference.md) |
| **Python Data Types** | Hierarchy/mutability tree, core built-in types (Numbers, Sequences, Mappings, Sets) summary, and type casting. | [Go to Data Types 📊](./01_basics/datatype.md) |
| **Numbers Deep Dive** | Integers (unlimited precision, caching optimization), Floats (precision issues, special values), complex numbers, fractions, decimals. | [Go to Numbers 🔢](./01_basics/numbers.md) |
| **Strings Deep Dive** | String creation & multiline blocks, indexing & slicing, formatting (F-strings), raw strings (`r""`), and core methods. | [Go to Strings 🧵](./01_basics/string.md) |
| **Lists Deep Dive** | List operations & slicing, mutability, slice reassignment, and list modification gotchas/best practices. | [Go to Lists 📋](./01_basics/list.md) |
| **Dictionaries Deep Dive** | Dictionary creation, value retrieval (brackets vs `.get()`), key modifications, iteration methods, and length. | [Go to Dictionaries 📖](./01_basics/dictionary.md) |
| **Tuples Deep Dive** | Why we use tuples, immutability compared to lists, slicing, operators, counts, unpacking, and nesting. | [Go to Tuples 🧠](./01_basics/tuple.md) |

---

### 2️⃣ Chapter 02: Python Conditionals
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Conditional Problems** | 10 control flow questions covering Age, Ticket Pricing, Grades, Ripeness, Weather, Transport, Coffee, Password Strength, Leap Years, and Pet Food. | [Go to Conditionals ⚡](./02_conditionals/questions.md) |

---

### 3️⃣ Chapter 03: Python Loops
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Loop Problems** | Practice questions covering `for` loops, `while` loops, break/continue, prime checks, and duplication detectors. | [Go to Loops 🔄](./03_loop/questions.md) |

---

### 4️⃣ Chapter 04: Iteration Tools Under the Hood
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Iteration Mechanics** | Iterables vs Iterators, `iter()` & `next()`, file cursor vs list iterator memory references, dictionary & range iteration under the hood. | [Go to Iteration Notes ⚙️](./04_iteration_tools/iteration.md) |
| **Interview Q&A** | Top interview questions on iteration protocol, custom iterable classes, generators (`yield`), and memory behaviors. | [Go to Iteration Interview Q&A 🎯](./04_iteration_tools/interview_questions.md) |

---

### 5️⃣ Chapter 05: Python Functions
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Functions Deep Dive** | Functions as objects, Pass-by-Object-Reference, Call Stack & Frames, LEGB rule, `*args`, `**kwargs`, Closures (`__closure__`), and `yield` Generators. | [Go to Functions Deep Dive ⚙️](./05_functions/functions.md) |
| **Functions Practice Problems** | 10 practice problems covering Basic Syntax, Multiple Parameters, Polymorphism, Multiple Return Values, Default Values, Lambda, `*args`, `**kwargs`, Generators, and Recursion. | [Go to Function Problems 📝](./05_functions/question.md) |

---

### 6️⃣ Chapter 06: Python Scopes
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Scopes & LEGB Rule** | Local, Enclosing, Global, and Built-in scopes explained with the Magic Glasses & Neighborhood analogies, `global` vs `nonlocal` keywords, and Lexical Scope. | [Go to Scopes Guide 👓](./06_scopes/scopes.md) |
| **Scope Code Examples** | Executable script demonstrating `global` and `nonlocal` variable modifications in action. | [Go to Scope Script 🐍](./06_scopes/01_scope.py) |

---

### 7️⃣ Chapter 07: Object-Oriented Programming (OOPs)
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **OOP Easy Guide** | The Car Factory analogy explaining Class vs Object, `self`, `__init__`, the 4 Pillars (Inheritance, Encapsulation, Polymorphism, Abstraction), Class Variables, Static Methods, and `@property`. | [Go to OOP Easy Guide 🏎️](./07_oops/oops.md) |
| **OOP Problems & Concepts** | 10 problems covering Classes, Instances, `self`, Inheritance, Encapsulation, Polymorphism, Class Variables, Static Methods, `@property` Decorators, `isinstance()`, and Multiple Inheritance. | [Go to OOP Questions 🚗](./07_oops/questions.md) |

---

### 8️⃣ Chapter 08: Python Decorators
| Topic | Key Focus Areas | Link |
| :--- | :--- | :--- |
| **Decorator Problems** | 3 core practice problems covering Timing Function Execution, Debugging Function Calls, and Caching Return Values. | [Go to Decorator Questions 🎨](./08_decorators/questions.md) |

---

## 🚀 How to Run Python Scripts

To run any script in this repository, navigate to the root directory or specific folder and run:

```bash
python <script_name>.py
```

For example:
```bash
python 05_functions/07_solution.py
python 06_scopes/01_scope.py
```
