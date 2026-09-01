# Python User Input 

## 📌 Introduction

Python provides the `input()` function to take input from the user through the keyboard.

The `input()` function pauses the program and waits for the user to enter something.

### Syntax

```python
input("message")
```

The message inside `input()` is displayed to the user as a prompt.

---

# 🔹 `input()` Function

The `input()` function takes user input as a **string**.

```python
# input

# takes input as a string

name = input("Enter name : ")

print(name)

age = input("Enter age : ")

print(age)
```

If the user enters:

```text
Enter name : Kushagra
Enter age : 21
```

The values stored in `name` and `age` will both be strings.

Conceptually:

```python
name = "Kushagra"  # str
age = "21"         # str
```

> 📌 Even though `21` looks like a number, `input()` stores it as a string.

---

# 🔹 Taking Numeric Input

If you want to use the user's input as a number, you need to **convert** the string into the required data type.

### Integer Input

Use `int()` to convert the input into an integer.

```python
age = int(input("Enter age : "))

print(age)
```

Now `age` will contain an integer.

### Float Input

Use `float()` to convert the input into a floating-point number.

```python
height = float(input("Enter height : "))

print(height)
```

---

# 🔹 Checking the Input Type

You can use the `type()` function to check the data type of the input.

```python
age = input("Enter age : ")

print(age)
print(type(age))
```

For an input such as `21`, the output will be:

```text
21
<class 'str'>
```

This demonstrates that `input()` returns a string.

---

# 🧠 Important Notes

* `input()` is used to take input from the user.
* The program waits for the user to enter a value.
* `input()` **always returns a string**.
* Use `int()` when an integer is required.
* Use `float()` when a decimal number is required.
* Use `type()` to check the data type of a value.

---

# 🚀 Quick Summary

| Function  | Purpose                          |
| --------- | -------------------------------- |
| `input()` | Takes user input as a string     |
| `int()`   | Converts a value to an integer   |
| `float()` | Converts a value to a float      |
| `type()`  | Returns the data type of a value |

---
