# Python If-Else Statements

## 📌 Introduction

Conditional statements are used to make **decisions** in a Python program.

They allow a program to execute different blocks of code depending on whether a condition is `True` or `False`.

Python provides three commonly used conditional statements:

* `if`
* `elif`
* `else`

---

# 🔹 `if` Statement

The `if` statement executes a block of code only when its condition is `True`.

### Syntax

```python
if condition:
    # code to execute
```

> 📌 Python uses **indentation** to define the block of code belonging to an `if` statement.

---

# 🔹 `if-else` Statement

The `else` block executes when the `if` condition is `False`.

### Syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

---

# 💻 Practice Program — Email and Password

In this example, we check whether the user entered a valid email and password.

### Correct Credentials

```text
Email: kushagra@example.com
Password: pass123
```

### Program

```python
# ============ if else ===============

# correct email - kushagra@example.com
# correct password - pass123

email = input("Enter your Email : ")

if '@' in email:

    password = input("Enter your Password : ")

    if email == "kushagra@example.com" and password == "pass123":

        print("Welcome!!")

    else:

        print("Wrong Credentials")

else:

    print("Email is wrong Give correct email")
```

---

## 🔍 Understanding the Program

First, the program asks the user for an email:

```python
email = input("Enter your Email : ")
```

Then it checks whether the email contains `@`:

```python
if '@' in email:
```

The `in` operator checks whether `@` exists inside the string.

If it exists, the program asks for the password:

```python
password = input("Enter your Password : ")
```

Then both credentials are checked:

```python
if email == "kushagra@example.com" and password == "pass123":
```

The `and` operator means **both conditions must be true**.

If both are correct:

```text
Welcome!!
```

Otherwise:

```text
Wrong Credentials
```

If the email doesn't contain `@`, the password isn't requested and the program displays:

```text
Email is wrong Give correct email
```

---

# 🔹 Nested `if`

An `if` statement can be placed inside another `if` statement. This is called a **nested if statement**.

In the previous example:

```python
if '@' in email:

    password = input("Enter your Password : ")

    if email == "kushagra@example.com" and password == "pass123":
        print("Welcome!!")
```

The second `if` is inside the first `if`.

The password check only happens when the email contains `@`.

---

# 🔹 `elif` Statement

`elif` stands for **else if**.

It allows you to check another condition when the previous `if` condition is `False`.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

Python checks the conditions from top to bottom.

---

# 💻 Giving the User a Second Chance

The following example gives the user another chance when the email is correct but the password is incorrect.

```python
# ============ Give user a second chance ===============

if email == "kushagra@example.com" and password == "pass123":

    print("Welcome!!")

elif email == "kushagra@example.com" and password != "pass123":

    print("Password incorrect")

    password = input("Enter password again : ")

    if password == "pass123":

        print("Finally Correct!! Welcome")

    else:

        print("Still incorrect")

else:

    print("Wrong Credentials")
```

---

# 🔍 Understanding `elif`

The first condition checks whether **both email and password are correct**:

```python
if email == "kushagra@example.com" and password == "pass123":
```

If this is true:

```text
Welcome!!
```

If it is false, Python checks the `elif` condition:

```python
elif email == "kushagra@example.com" and password != "pass123":
```

This checks whether:

* The email is correct.
* The password is incorrect.

If both are true, the user gets another opportunity to enter the password.

---

# 🔹 Comparison Operators in the Example

The program uses comparison operators such as:

```python
==
!=
```

### `==`

Checks whether two values are equal.

```python
email == "kushagra@example.com"
```

### `!=`

Checks whether two values are not equal.

```python
password != "pass123"
```

---

# 🔹 Logical `and`

The `and` operator combines two conditions.

```python
email == "kushagra@example.com" and password == "pass123"
```

Both conditions must be `True`.

| Email   | Password | Result  |
| ------- | -------- | ------- |
| Correct | Correct  | `True`  |
| Correct | Wrong    | `False` |
| Wrong   | Correct  | `False` |
| Wrong   | Wrong    | `False` |

---

# 🔹 Indentation

Indentation is extremely important in Python.

For example:

```python
if True:
    print("Hello")
```

The indented `print()` belongs to the `if` statement.

Python commonly uses **4 spaces** for indentation.

Incorrect indentation can result in an error.

---

# 🧠 Important Notes

* `if` is used to check a condition.
* `elif` checks another condition when previous conditions are false.
* `else` executes when none of the preceding conditions are true.
* Multiple `elif` statements can be used.
* An `if` statement can be nested inside another `if`.
* Conditions generally produce `True` or `False`.
* Python uses indentation to define code blocks.
* `and` requires all connected conditions to be true.
* `in` checks whether a value exists inside a sequence or collection.

---

# 🚀 Quick Summary

| Statement   | Purpose                                     |
| ----------- | ------------------------------------------- |
| `if`        | Executes code when a condition is true      |
| `elif`      | Checks another condition                    |
| `else`      | Executes when previous conditions are false |
| Nested `if` | An `if` statement inside another statement  |

---

# 💡 Basic Example

```python
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Adult
```

---

# 🎯 Key Takeaway

Conditional statements allow your program to **make decisions**.

The basic structure to remember is:

```python
if condition:
    # runs when condition is True

elif another_condition:
    # runs when another condition is True

else:
    # runs when all conditions are False
```

Think of it as:

```text
        Condition?
           |
       +---+---+
       |       |
     True    False
       |       |
      if      elif?
               |
          +----+----+
          |         |
        True      False
          |         |
        elif      else
```

> 💡 **Key Takeaway:** `if`, `elif`, and `else` are the foundation of decision-making in Python programs.
