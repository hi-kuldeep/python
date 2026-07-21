# Python Error Handling & Resource Management 🛡️

In Python, errors happen when code runs into unexpected situations (e.g., dividing by zero, missing files, or network drops). 

Error handling ensures your program doesn't crash abruptly, and **Resource Management** ensures files or connections are closed cleanly.

---

## 🛡️ 1. The `try...except...else...finally` Block

* **`try`**: The block of code to test for errors.
* **`except`**: Code that runs if an error occurs inside `try`.
* **`else`**: Code that runs only if **no error** occurred inside `try`.
* **`finally`**: Code that **ALWAYS runs**, regardless of whether an error occurred or not (great for cleanup!).

```python
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()  # Always executes to close the file handle
```

---

## 🔒 2. Context Managers (`with` statement)

Instead of manually writing `try...finally` to close files, Python provides a cleaner and safer pattern called a **Context Manager** using the `with` keyword.

```python
# Automatically handles opening and closing the file cleanly
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')
```

### Why use `with`?
1. **Cleaner Code**: No need to manually call `file.close()`.
2. **Automatic Cleanup**: Automatically closes the file stream even if an exception is thrown inside the `with` block.
