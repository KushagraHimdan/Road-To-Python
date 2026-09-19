# Python Variables

## 📌 Introduction

Variables are used to store data in a Python program.

Unlike some programming languages, Python does not require you to explicitly declare a variable's data type before assigning a value to it.

---

# 🔹 Variable Assignment

In Python, a variable is created when a value is assigned to it using the assignment operator `=`.

```python
name = "Kushagra"

print(name)

age = 21

print(age)
```

Here:

* `name` stores the string `"Kushagra"`
* `age` stores the integer `21`

---

# 🔹 No Explicit Variable Declaration

Languages such as Java and C++ usually require variables to be declared with a specific data type.

For example, in Java:

```java
String name = "Kushagra";
int age = 21;
```

However, Python automatically determines the type based on the assigned value.

```python
name = "Kushagra"
age = 21
```

This makes Python easier and faster to write.

---

# 🔹 Dynamic Typing

Python is a **dynamically typed language**.

This means Python automatically determines the data type of a variable based on the value assigned to it.

```python
name = "kush"  # name -> string

print(name)

name = 4  # name -> integer

print(name)

name = True  # name -> boolean

print(name)
```

The same variable can refer to values of different data types at different points in the program.

---

# 🔹 Dynamic Typing vs Static Typing

## Dynamic Typing

The data type is automatically determined by the programming language.

Examples include:

* Python
* PHP
* JavaScript

## Static Typing

The data type is explicitly declared and is checked according to the language's type system.

Examples include:

* Java
* C
* C++

For example, in Java:

```java
String name = "Kushagra";
```

Here, the variable is explicitly declared as a `String`.

---

# 🔹 Dynamic Binding

Python supports **dynamic binding**, meaning a variable name can be associated with objects of different data types during the execution of a program.

```python
name = "Kushagra"

name = 21

name = True
```

The variable `name` refers to a different type of value each time a new value is assigned.

---

# 🔹 Static Binding

In statically typed languages, variables are generally associated with a declared type.

For example:

```java
int age = 21;
```

The variable `age` is declared to store integer values.

---

# 🔹 Special Declaration Syntax

Python provides several convenient ways to assign values to variables.

---

## 1️⃣ Multiple Statements on One Line

You can declare multiple variables on the same line.

```python
a = 5; b = 6; c = 7

print(a)

print(b)

print(c)
```

Although this is valid Python syntax, writing each statement on a separate line is generally easier to read.

---

## 2️⃣ Multiple Variable Assignment

You can assign multiple values to multiple variables in a single statement.

```python
a, b, c = 8, 9, 10

print(a)

print(b)

print(c)
```

Here:

* `a` gets `8`
* `b` gets `9`
* `c` gets `10`

---

## 3️⃣ Assigning the Same Value to Multiple Variables

You can assign the same value to multiple variables.

```python
a = b = c = 4

print(a)

print(b)

print(c)
```

All three variables receive the value `4`.

---

# 🧠 Important Notes

* Python does not require explicit data type declarations for variables.
* Variables are created when values are assigned to them.
* Python is dynamically typed.
* A variable can refer to objects of different types at different times.
* Variable names should be meaningful and easy to understand.
* Python variable names are case-sensitive.

For example:

```python
name = "Kushagra"
Name = "Python"
```

`name` and `Name` are considered two different variables.

---

# 📌 Variable Naming Rules

When creating variables in Python:

✅ Variable names can contain:

* Letters
* Numbers
* Underscores (`_`)

❌ Variable names cannot:

* Start with a number
* Contain spaces
* Use special characters such as `@`, `#`, or `-`
* Use Python reserved keywords

### Valid Examples

```python
name = "Kushagra"
student_age = 21
age1 = 21
```

### Invalid Examples

```python
# 1name = "Kushagra"
# student age = 21
# student-name = "Kushagra"
```

---

# 🚀 Quick Summary

| Concept               | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| Variable              | Stores a reference to a value/object                              |
| Dynamic Typing        | Python determines the type automatically                          |
| Static Typing         | The type is explicitly declared in languages such as Java and C++ |
| Dynamic Binding       | A name can be rebound to objects of different types               |
| Multiple Assignment   | Multiple variables can receive values in one statement            |
| Same Value Assignment | Multiple variables can be assigned the same value                 |

---