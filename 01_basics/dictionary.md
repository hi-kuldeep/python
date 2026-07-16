# Python Dictionaries: Deep Dive 📖

In Python, a dictionary is a mutable, unordered (preserved insertion order since Python 3.7) collection of key-value pairs. Dictionaries are optimized for retrieving values when you know the key.

---

## 📌 1. Creating & Accessing Dictionaries

### Creating a Dictionary
Dictionaries are created using curly braces `{}` with key-value pairs separated by colons:
```python
flavors = {
    "Apple": "Sweet",
    "Lemon": "Sour",
    "Orange": "Tangy"
}
```

### Accessing Values
There are two primary ways to access values in a dictionary:

#### 1. Bracket Notation (`dict[key]`)
```python
print(flavors["Apple"]) # Output: "Sweet"
```
> [!CAUTION]
> **Gotcha:** If the key does not exist, bracket notation throws a **`KeyError`**:
> ```python
> print(flavors["Mango"]) # Raises KeyError: 'Mango'
> ```

#### 2. The `.get(key)` Method (Recommended 🚀)
```python
print(flavors.get("Lemon"))  # Output: "Sour"
```
> [!TIP]
> If the key does not exist, `.get()` returns **`None`** instead of crashing. You can also specify a default fallback value:
> ```python
> print(flavors.get("Mango"))                 # Output: None
> print(flavors.get("Mango", "Unknown Flavor")) # Output: "Unknown Flavor"
> ```

---

## ✏️ 2. Modifying and Adding Elements

Dictionaries are mutable. You can add new key-value pairs or modify existing ones using bracket assignment:

```python
flavors = {
    "Apple": "Sweet",
    "Lemon": "Sour",
    "Orange": "Tangy"
}

# Modifying an existing key
flavors["Orange"] = "Zesty"

# Adding a new key
flavors["Lime"] = "Acidic"

print(flavors)
# Output: {'Apple': 'Sweet', 'Lemon': 'Sour', 'Orange': 'Zesty', 'Lime': 'Acidic'}
```

---

## 🔁 3. Iteration & Membership

### Iterating Through a Dictionary
By default, iterating over a dictionary loops through its **keys**:

```python
flavors = {"Apple": "Sweet", "Lemon": "Sour", "Orange": "Zesty"}

# Method A: Iterating through keys
for fruit in flavors:
    print(fruit)
# Output:
# Apple
# Lemon
# Orange

# Method B: Iterating through keys and accessing values
for fruit in flavors:
    print(fruit, flavors[fruit])
# Output:
# Apple Sweet
# Lemon Sour
# Orange Zesty

# Method C: Using .items() (Most Pythonic & Readable 🚀)
for fruit, taste in flavors.items():
    print(fruit, taste)
# Output:
# Apple Sweet
# Lemon Sour
# Orange Zesty
```

### Membership Testing (`in` operator)
The `in` operator checks if a **key** exists in the dictionary:
```python
print("Apple" in flavors)  # Output: True
print("Sweet" in flavors)  # Output: False (Checks keys, not values)
```

### Checking Dictionary Length (`len()`)
Returns the number of key-value pairs:
```python
print(len(flavors)) # Output: 3
```

---

## 🛠️ 4. Core Dictionary Methods

Here are other essential dictionary methods using generic names and values:

* **`.pop(key)`**: Removes the specified key and returns its value.
* **`.popitem()`**: Removes and returns the last inserted key-value pair as a tuple `(key, value)`.
* **`del dict[key]`**: Deletes the specified key from the dictionary.
* **`.clear()`**: Removes all elements, leaving an empty dictionary `{}`.
* **`.copy()`**: Returns a shallow copy of the dictionary.

```python
flavors = {"Apple": "Sweet", "Lemon": "Sour", "Orange": "Tangy"}

# 1. Pop (by key)
removed_taste = flavors.pop("Lemon") 
# removed_taste: "Sour"
# flavors is now: {"Apple": "Sweet", "Orange": "Tangy"}

# 2. Popitem (removes last inserted item)
last_item = flavors.popitem() 
# last_item: ("Orange", "Tangy")
# flavors is now: {"Apple": "Sweet"}

# 3. Del (by key)
del flavors["Apple"] 
# flavors is now: {} (empty)

# 4. Clear
flavors = {"Apple": "Sweet", "Lemon": "Sour"}
flavors.clear() 
# flavors is now: {}

# 5. Copy (Shallow Copy)
flavors = {"Apple": "Sweet", "Lemon": "Sour"}
flavors_copy = flavors.copy()
```

---

## 🪆 5. Nested Dictionaries

Dictionaries can store other dictionaries as values, enabling representation of complex, hierarchical data.

```python
catalog = {
    "fruits": {
        "Apple": "Sweet",
        "Lemon": "Sour"
    },
    "vegetables": {
        "Carrot": "Sweet",
        "Broccoli": "Bitter"
    }
}

# Accessing the nested dictionary
print(catalog["fruits"]) 
# Output: {"Apple": "Sweet", "Lemon": "Sour"}

# Accessing a value inside the nested dictionary
print(catalog["fruits"]["Lemon"]) 
# Output: "Sour"
```

---

## ⚡ 6. Dictionary Comprehensions

You can generate dictionaries dynamically using comprehensions.
**Syntax:** `{key_expression: value_expression for item in iterable}`

```python
# Create a dictionary of squares for numbers 0 to 5
squared_num = {x: x**2 for x in range(6)}

print(squared_num)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## ⚠️ 7. Dictionary Gotchas & Traps

### ❌ Trap: The `dict.fromkeys()` Reference Sharing Gotcha
> [!WARNING]
> When using `dict.fromkeys(keys, default_value)`, if the `default_value` is a **mutable object** (like a list or a dictionary), **all keys share the exact same object reference in memory**.
>
> ```python
> keys = ["Apple", "Banana", "Cherry"]
> default_list = ["Fruit"]
> 
> new_dict = dict.fromkeys(keys, default_list)
> print(new_dict)
> # Output: {'Apple': ['Fruit'], 'Banana': ['Fruit'], 'Cherry': ['Fruit']}
> 
> # Mutating the list for one key...
> new_dict["Apple"].append("Tasty")
> 
> # ...mutates it for ALL keys!
> print(new_dict)
> # Output: {'Apple': ['Fruit', 'Tasty'], 'Banana': ['Fruit', 'Tasty'], 'Cherry': ['Fruit', 'Tasty']}
> ```
>
> **✅ Correct / Best Practice:** To create independent mutable objects for each key, use a dictionary comprehension instead:
> ```python
> new_dict = {key: ["Fruit"] for key in keys}
> new_dict["Apple"].append("Tasty")
> print(new_dict)
> # Output: {'Apple': ['Fruit', 'Tasty'], 'Banana': ['Fruit'], 'Cherry': ['Fruit']}
> ```
