# Python Keywords and Identifiers 

## 📌 Introduction

While writing Python programs, we use different names for variables, functions, classes, modules, and other objects. These names are called **identifiers**.

However, some words already have special meanings in Python. These reserved words are called **keywords**.

---

# 🔹 Keywords

A **keyword** is a reserved word that has a special meaning and purpose in the Python programming language.

Keywords are used by Python to define the structure and syntax of a program.

Because keywords have special meanings, they **cannot be used as variable names, function names, or other identifiers**.

For example:

```python
# This is invalid because 'if' is a Python keyword

# if = 10
```

---

## 🔍 Finding Python Keywords

Python provides the `keyword` module, which can be used to view the list of keywords available in your Python version.

```python
# keyword

import keyword

print(keyword.kwlist)
```

The output will display all the keywords available in the version of Python you are using.

> 📌 **Note:** The number of Python keywords can vary depending on the Python version. Therefore, using `keyword.kwlist` is the best way to check the keywords available in your installed version.

---

# 🔹 Important Note: Python is Case-Sensitive

Python is a **case-sensitive programming language**.

This means uppercase and lowercase letters are treated differently.

For example:

```python
name = "Kushagra"
Name = "Python"

print(name)
print(Name)
```

Here, `name` and `Name` are two different identifiers.

Similarly, Python keywords must be written using their correct lowercase form.

For example:

```python
# Correct
if True:
    print("Hello")

# Incorrect
# If True:
#     print("Hello")
```

---

# 🔹 Identifiers

An **identifier** is a name used to identify different elements in a Python program.

Identifiers can be used to name:

* Variables
* Functions
* Classes
* Modules
* Objects

For example:

```python
name = "Kushagra"  # name is an identifier

_ = 98  # _ can be used as an identifier

print(_)
```

In this example:

* `name` is an identifier.
* `_` is also a valid identifier.

---

# 📌 Rules for Creating Identifiers

Python identifiers must follow certain rules.

## 1️⃣ Must Start With a Letter or Underscore

An identifier can start with:

* An alphabet letter (`A-Z` or `a-z`)
* An underscore (`_`)

### Valid Examples

```python
name = "Kushagra"
_age = 21
```

### Invalid Example

```python
# 1name = "Kushagra"
```

An identifier cannot start with a digit.

---

## 2️⃣ Can Contain Letters, Digits, and Underscores

After the first character, an identifier can contain:

* Letters
* Digits
* Underscores (`_`)

### Valid Examples

```python
student_name = "Kushagra"
age21 = 21
student_1 = "Python"
```

---

## 3️⃣ Keywords Cannot Be Used as Identifiers

Python keywords have reserved meanings and cannot be used as identifiers.

### Invalid Example

```python
# class = "Python"
```

Since `class` is a Python keyword, it cannot be used as a variable name.

---

## 4️⃣ Identifiers Cannot Contain Spaces

Spaces are not allowed in identifiers.

### Invalid Example

```python
# student name = "Kushagra"
```

### Correct Version

```python
student_name = "Kushagra"
```

---

## 5️⃣ Identifiers Cannot Use Special Characters

Special characters such as:

```text
@ # $ % -
```

cannot normally be used in identifiers.

### Invalid Example

```python
# student-name = "Kushagra"
# student@name = "Kushagra"
```

The underscore `_` is the commonly allowed special character used in Python identifiers.

---

# 🧠 Quick Summary

| Concept            | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| Keyword            | A reserved word with a special meaning in Python                         |
| Identifier         | A name used to identify variables, functions, classes, and other objects |
| Case Sensitive     | `name` and `Name` are different                                          |
| Starting Character | Must start with a letter or `_`                                          |
| Digits             | Can be used after the first character                                    |
| Keywords           | Cannot be used as identifiers                                            |

---

# 💡 Complete Example

```python
# ================= Keywords ===================

# Display all keywords available in the current Python version

import keyword

print(keyword.kwlist)


# ================= Identifiers ===================

name = "Kushagra"  # name is an identifier

_ = 98  # _ can be used as an identifier

print(_)
```

---

# 🚀 Key Takeaway

**Keywords** are reserved words that have special meanings in Python and cannot be used as identifiers.

**Identifiers** are names given to variables, functions, classes, modules, and other objects.

When creating identifiers, remember:

* Start with a letter or `_`
* Use letters, digits, and `_`
* Do not use spaces
* Do not use reserved keywords
* Remember that Python is case-sensitive
