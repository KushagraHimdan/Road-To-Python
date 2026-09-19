# Python Comments 💬

## 📌 Introduction

Comments are used to add explanations, notes, or descriptions to Python code.

Comments help developers understand the purpose and functionality of the code. Python ignores comments when executing a program.

Comments are especially useful when:

* Explaining code
* Making code easier to understand
* Adding notes for future reference
* Temporarily disabling code during testing

---

# 🔹 Single-Line Comments

In Python, a single-line comment starts with the `#` symbol.

Anything written after `#` is ignored by the Python interpreter.

## Syntax

```python
# This is a comment
```

## Example

```python
# Single line comment

print("Hello, World!")
```

In the example above:

```python
# Single line comment
```

is ignored by Python, while:

```python
print("Hello, World!")
```

is executed.

---

# 🔹 Comments After Code

A comment can also be written after a line of code.

```python
print("Hello")  # This prints Hello
```

The comment after `#` is ignored during program execution.

---

# 🔹 Multiple Single-Line Comments

You can use multiple single-line comments to explain different parts of your code.

```python
# Store a name
name = "Kushagra"

# Print the name
print(name)
```

---

# 🔹 Multi-Line Comments

Python does not have a dedicated multi-line comment syntax like some programming languages.

However, multiple lines can be commented by placing `#` at the beginning of each line.

```python
# This is the first line of a comment
# This is the second line of a comment
# This is the third line of a comment
```

---

# 🔹 Using Triple Quotes

Triple quotes are sometimes used to write multi-line text.

```python
"""
This is a multi-line text.
It can span across multiple lines.
"""
```

> 📌 Triple-quoted strings are technically **strings**, not actual comments. However, they are sometimes used for documentation purposes.

---

# 🧠 Important Notes

* Comments begin with the `#` symbol.
* Python ignores comments during execution.
* Comments help make code more readable and understandable.
* Good comments explain **why** something is being done, rather than simply repeating what the code already says.

---

# 🚀 Quick Summary

| Type                 | Syntax                           |
| -------------------- | -------------------------------- |
| Single-line Comment  | `# Comment`                      |
| Multiple Lines       | Multiple lines starting with `#` |
| Documentation String | `""" Text """`                   |

---

## 💡 Example

```python
# ================= Comments ===================

# Single line comment

print("This code will run!")

# print("This code will not run because it is commented out")
```

The first `print()` statement executes normally, while the second one is ignored because it is commented out.
