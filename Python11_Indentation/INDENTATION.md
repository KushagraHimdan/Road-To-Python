# Python Indentation

## What is Indentation?

**Indentation** means the spaces at the beginning of a line of code.

In Python, indentation is **very important** because it is used to define a **block of code**.

Unlike languages such as C, C++, and Java, Python does not use `{}` braces to define code blocks. Instead, Python uses **indentation**.

---

## Basic Example

```python
# ====================== Indentation ===================

topic = input("Enter topic : ")

if topic == "indentation":

    print("Indentation is the space to specify the block of code")

else:

    print("wrong topic!!")
```

### How it works

```python
if topic == "indentation":
    print("Indentation is the space to specify the block of code")
```

The `print()` statement is indented, which tells Python that it belongs to the `if` block.

Similarly:

```python
else:
    print("wrong topic!!")
```

The `print()` statement belongs to the `else` block because it is indented.

---

## Indentation Rules

### 1. Indentation defines a code block

```python
if True:
    print("Inside if")
```

Here, the indented `print()` statement belongs to the `if` statement.

---

### 2. Python commonly uses 4 spaces

The recommended indentation in Python is **4 spaces**.

```python
if age >= 18:
    print("Adult")
```

Avoid mixing tabs and spaces in the same file.

---

### 3. Incorrect indentation causes an error

```python
if True:
print("Hello")
```

This produces an `IndentationError` because Python expects the statement inside the `if` block to be indented.

Correct:

```python
if True:
    print("Hello")
```

---

## Indentation with Multiple Statements

Multiple statements can belong to the same block:

```python
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can drive")
```

All three statements have the same indentation, so they belong to the `if` block.

---

## Nested Indentation

Indentation can also be used for **nested blocks**.

```python
age = 20

if age >= 18:
    print("Adult")

    if age >= 21:
        print("21 or older")
```

Here, the second `if` is inside the first `if`, so it has another level of indentation.

---

## Indentation with Loops

Indentation is also required with loops.

```python
for i in range(5):
    print(i)
```

The `print()` statement is inside the `for` loop because it is indented.

---

## Indentation with Functions

Functions also use indentation to define their body.

```python
def greet():
    print("Hello")
    print("Welcome to Python")

greet()
```

Both `print()` statements belong to the `greet()` function.

---

## Important Point

Python uses indentation to determine **where a block starts and ends**.

For example:

```python
if True:
    print("Statement 1")
    print("Statement 2")

print("Statement 3")
```

`Statement 1` and `Statement 2` are inside the `if` block.

`Statement 3` is outside the block because it is not indented.

---

## Common Indentation Errors

### ❌ Missing indentation

```python
if True:
print("Hello")
```

### ✅ Correct

```python
if True:
    print("Hello")
```

### ❌ Inconsistent indentation

```python
if True:
    print("Hello")
      print("World")
```

The indentation level should be consistent within the same block.

---

## Key Takeaways

| Concept               | Description                                           |
| --------------------- | ----------------------------------------------------- |
| Indentation           | Spaces at the beginning of a line                     |
| Purpose               | Defines blocks of code                                |
| Recommended           | 4 spaces                                              |
| Used with             | `if`, `else`, `elif`, loops, functions, classes, etc. |
| Braces `{}`           | Not required for code blocks                          |
| Incorrect indentation | Can cause `IndentationError`                          |

### Remember

> **In Python, indentation is not just for readability — it is part of the syntax.**
