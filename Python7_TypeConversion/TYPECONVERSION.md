# Python Type Conversion 🔄

## 📌 Introduction

**Type conversion** means converting a value from one data type to another.

Python supports two main types of conversion:

1. **Implicit Type Conversion** — Python automatically converts the type.
2. **Explicit Type Conversion** — The programmer manually converts the type.

Type conversion is especially important when working with user input because Python's `input()` function always returns a string.

---

# 🔹 Practice Program — Add Two Numbers

Let's first see what happens when we try to add two numbers taken using `input()`.

```python
# Practice program -> add two numbers

num1 = input("First number : ")  # 2

num2 = input("Second number : ")  # 4

res = num1 + num2  # 2 + 4

print("Sum is : ", res)  # Sum is : 24

print(type(num1))  # class -> str

print(type(num2))  # class -> str

print(type(res))  # class -> str
```

If the user enters:

```text
First number : 2
Second number : 4
```

The output will be:

```text
Sum is : 24
```

This happens because `input()` takes input as a **string**.

So Python is actually performing:

```python
"2" + "4"
```

which results in:

```text
"24"
```

It is **concatenating** two strings rather than performing numerical addition.

> 📌 **Key Point:** `input()` always returns a value of type `str`.

---

# 🔹 Why Does Python Take Input as a String?

Python takes user input as a string because text is a flexible and general format for receiving information from a user.

For example:

```python
age = input("Enter age : ")
```

Even if the user enters:

```text
21
```

Python stores it as:

```python
"21"
```

If you need it as an integer, you have to explicitly convert it:

```python
age = int(input("Enter age : "))
```

---

# 🔹 Implicit Type Conversion

**Implicit type conversion** happens automatically.

Python automatically converts one data type into another when it is safe and appropriate to do so.

### Example

```python
# implicit type conversion : Type conversion automatically

res2 = 4 + 5.5

print(res2)

print(type(res2))  # float
```

Here:

* `4` is an `int`
* `5.5` is a `float`

Python automatically converts the integer into a floating-point value before performing the addition.

The result is:

```text
9.5
<class 'float'>
```

---

## 🔹 Integer + Complex

```python
res3 = 4 + 5+7j

print(res3)

print(type(res3))  # complex
```

Python automatically converts the integer values into a compatible numeric representation for the complex calculation.

Output:

```text
9+7j
<class 'complex'>
```

---

## 🔹 Float + Complex

```python
res4 = 4.7 + 5+7j

print(res4)

print(type(res4))  # complex
```

Output:

```text
9.7+7j
<class 'complex'>
```

The result is a `complex` value.

---

# 🔹 Explicit Type Conversion

**Explicit type conversion** means that the programmer manually tells Python which type a value should be converted to.

Python provides built-in functions such as:

```text
int()
float()
str()
bool()
complex()
list()
```

---

## 🔹 Converting to Integer

```python
res5 = int(4 + 5.5)

print(res5)  # 9

print(type(res5))  # int
```

Here:

```python
4 + 5.5
```

first produces:

```text
9.5
```

Then:

```python
int(9.5)
```

converts it to:

```text
9
```

> ⚠️ Converting a float to an integer removes the decimal portion. It does not round the number.

---

## 🔹 String to Integer

```python
res6 = 4 + int("56")

print(res6)  # 60

print(type(res6))  # int
```

Here:

```python
"56"
```

is converted from a string to an integer using `int()`.

> 📌 The original comment `# 9` would be incorrect here. The actual result is **60**.

---

## 🔹 Converting to String

```python
res7 = str(6)

print(res7)

print(type(res7))
```

The integer `6` is converted into the string `"6"`.

The resulting type is:

```text
<class 'str'>
```

---

## 🔹 Converting to Boolean

```python
res8 = bool(1)

print(res8)

print(type(res8))
```

Output:

```text
True
<class 'bool'>
```

In Python, `1` converts to `True`.

Some common conversions include:

```python
bool(0)       # False
bool(1)       # True
bool("")      # False
bool("Hello") # True
```

---

## 🔹 Converting to Complex

```python
res9 = complex(6)

print(res9)

print(type(res9))
```

Output:

```text
(6+0j)
<class 'complex'>
```

The integer `6` is converted into a complex number.

---

## 🔹 Converting to List

```python
res10 = list("Kushagra")

print(res10)

print(type(res10))
```

Output:

```text
['K', 'u', 's', 'h', 'a', 'g', 'r', 'a']
<class 'list'>
```

The string is converted into a list containing its individual characters.

---

# 🔹 Type Conversion Is Not Permanent

Type conversion does **not permanently change the original value**.

Instead, conversion produces a new value of the requested type.

```python
# Type conversion Is not Permanent

# Actual value don't change

res11 = 8.9

print(res11)

print(int(res11))
```

Output:

```text
8.9
8
```

The original variable `res11` still contains:

```text
8.9
```

The expression:

```python
int(res11)
```

temporarily produces:

```text
8
```

It does not change `res11`.

If you wanted to permanently store the converted value, you would need to assign it back:

```python
res11 = int(res11)
```

---

# 🔹 Adding Two Numbers Correctly

Since `input()` returns strings, we can use `int()` to convert the input before performing the addition.

```python
# now

first_num = int(input("First number : "))

second_num = int(input("First number : "))

result = first_num + second_num

print("Sum is :", result)
```

Now, if the user enters:

```text
First number : 2
First number : 4
```

The result will be:

```text
Sum is : 6
```

The important part is:

```python
int(input(...))
```

The process is:

```text
User Input
    ↓
input()
    ↓
String
    ↓
int()
    ↓
Integer
    ↓
Addition
```

> 📌 Your second prompt says `"First number : "` again. If you want the prompt to correctly describe the second input, you can change it to `"Second number : "`. I have left your example otherwise unchanged.

---

# 🧠 Important Notes

* `input()` always returns a `str`.
* Type conversion changes the type of a value.
* **Implicit conversion** is performed automatically by Python.
* **Explicit conversion** is performed manually using functions such as `int()`, `float()`, and `str()`.
* Explicit conversion only works when the conversion is valid for the given value.
* Converting a value does not automatically modify the original variable.
* To keep a converted value, assign the result back to a variable.

---

# 🚀 Common Type Conversion Functions

| Function    | Converts To | Example                           |
| ----------- | ----------- | --------------------------------- |
| `int()`     | Integer     | `int("10")` → `10`                |
| `float()`   | Float       | `float("10.5")` → `10.5`          |
| `str()`     | String      | `str(10)` → `"10"`                |
| `bool()`    | Boolean     | `bool(1)` → `True`                |
| `complex()` | Complex     | `complex(10)` → `(10+0j)`         |
| `list()`    | List        | `list("ABC")` → `['A', 'B', 'C']` |

---

# 📌 Quick Summary

### Implicit Conversion

Python automatically converts the type.

```python
result = 4 + 5.5
```

### Explicit Conversion

The programmer manually converts the type.

```python
age = int("21")
```

### User Input

```python
age = input("Enter age : ")
```

`age` is a string.

### Numeric User Input

```python
age = int(input("Enter age : "))
```

`age` is an integer.

---

# 💡 Key Takeaway

> **`input()` → `str` → Convert when necessary**

Whenever you take numeric input from a user, remember to convert it before performing mathematical operations:

```python
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

result = num1 + num2

print(result)
```
