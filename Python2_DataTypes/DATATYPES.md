# Python Data Types 

## 📌 Introduction

Python provides different **data types** to represent and store different kinds of values. Every value in Python has a specific type that determines what kind of data it represents and what operations can be performed on it.

Python data types can broadly be categorized into three groups:

1. **Basic Types**
2. **Container Types**
3. **User-Defined Types**

---

# 🔹 1. Basic Types

Basic data types are used to store individual values.

The main basic types covered here are:

* `int` — Integer numbers
* `float` — Decimal or floating-point numbers
* `complex` — Complex numbers
* `bool` — Boolean values
* `str` — Text or strings

---

## 🔢 Integer (`int`)

Integers are whole numbers without a decimal point.

### Example

```python
# integer - any number
print(98)
```

Output:

```text
98
```

---

## 🔬 Large Numbers and Scientific Notation

Python can represent very large floating-point numbers using scientific notation.

```python
# max integer
print(1e308)

# inf
print(1e309)  # inf
```

> **Note:** `1e308` and `1e309` are represented as floating-point values in Python because scientific notation produces a `float`. Very large values beyond the floating-point limit can result in `inf` (infinity).

---

## 🔹 Float (`float`)

Floats are numbers that contain decimal points or are written using scientific notation.

### Example

```python
# float - decimal number
print(9.3)
```

Output:

```text
9.3
```

### Large Floating-Point Numbers

```python
# max float
print(1.7e308)

# inf
print(1.7e309)
```

> ⚠️ Extremely large floating-point values can exceed Python's floating-point range and become `inf`.

---

## ✅ Boolean (`bool`)

Boolean values represent one of two possible states:

* `True`
* `False`

### Example

```python
# boolean
print(True)

print(False)
```

---

## 🔷 Complex (`complex`)

Complex numbers contain a real part and an imaginary part.

Python uses `j` to represent the imaginary component.

### Example

```python
# complex - imaginary number
print(4+5j)
```

Here:

* `4` → Real part
* `5j` → Imaginary part

---

## 📝 String (`str`)

Strings are used to store textual data.

Python allows strings to be written using:

* Single quotes `' '`
* Double quotes `" "`
* Triple quotes `""" """`

### Examples

```python
# string
print('Apple')

print("Apple2")

print("""Apple2""")
```

Triple quotes are especially useful when working with **multi-line strings**.

---

# 📦 2. Container Types

Container data types are used to store multiple values together.

The main container types are:

* `list`
* `tuple`
* `set`
* `dictionary`

---

## 📋 List (`list`)

Lists store multiple values inside square brackets `[]`.

```python
# list
print([1, 2, 3, 4])
```

Lists are generally:

* Ordered
* Mutable (can be modified)
* Able to store different types of values

---

## 📌 Tuple (`tuple`)

Tuples store multiple values inside parentheses `()`.

```python
# tuple
print((1, 2, 3, 4))
```

Tuples are generally:

* Ordered
* Immutable (cannot be modified after creation)

---

## 🔸 Set (`set`)

Sets store unique values inside curly brackets `{}`.

```python
# sets
print({1, 2, 3, 4, 5})
```

Sets generally:

* Store unique values
* Are unordered
* Automatically remove duplicate values

---

## 📖 Dictionary (`dict`)

Dictionaries store data in **key-value pairs**.

```python
# dictionary
print({"Name":"Kushagra", "Age":21, "gender":"Male"})
```

In this example:

* `"Name"` → Key
* `"Kushagra"` → Value
* `"Age"` → Key
* `21` → Value

---

# 🏗️ 3. User-Defined Types

Python also allows developers to create their own data types.

The most common way to create a user-defined type is by using a **class**.

```python
class Student:
    pass
```

Classes allow you to create custom objects and organize related data and functionality together.

> 📌 Classes and object-oriented programming will be covered in more detail separately.

---

# 🧠 Quick Summary

| Category               | Data Types                               |
| ---------------------- | ---------------------------------------- |
| **Basic Types**        | `int`, `float`, `complex`, `bool`, `str` |
| **Container Types**    | `list`, `tuple`, `set`, `dict`           |
| **User-Defined Types** | `class`                                  |

---

# 🚀 Important Notes

* Python is a **dynamically typed language**, meaning you don't need to explicitly declare the data type of a variable.
* You can check the type of a value using the `type()` function.

### Example

```python
print(type(98))
print(type(9.3))
print(type(True))
print(type("Apple"))
```

Understanding data types is fundamental because almost every Python program works with different kinds of data.
