# Python Literals 

## 📌 Introduction

**Literals** are fixed or constant values written directly in the source code.

In simple words, literals are the **raw values assigned to variables**.

For example:

```python
age = 21
```

Here:

* `age` is a **variable**
* `21` is a **literal**

Python provides several types of literals:

1. Numeric Literals
2. String Literals
3. Boolean Literals
4. Special Literals

---

# 🔢 Numeric Literals

Numeric literals represent numbers in Python.

They can include:

* Binary literals
* Decimal literals
* Octal literals
* Hexadecimal literals
* Floating-point literals
* Complex literals

---

## 🔹 Integer Literals

Python supports different number systems for representing integers.

```python
# ================ Numeric Literals =========

a = 0b1010  # Binary literal

b = 100  # Decimal literal

c = 0o310  # Octal literal

d = 0x12c  # Hexadecimal literal
```

### Number System Prefixes

| Number System | Prefix    | Example  |
| ------------- | --------- | -------- |
| Binary        | `0b`      | `0b1010` |
| Decimal       | No prefix | `100`    |
| Octal         | `0o`      | `0o310`  |
| Hexadecimal   | `0x`      | `0x12c`  |

Although these values are written using different number systems, Python stores them as integers.

For example:

```python
print(a, b, c, d)
```

The output will be:

```text
10 100 200 300
```

---

# 🔹 Float Literals

Float literals represent decimal numbers.

```python
# Float literals

float_1 = 10.5

float_2 = 1.5e2

float_3 = 1.5e-3
```

Python also supports **scientific notation**.

### Examples

```python
1.5e2
```

means:

```text
1.5 × 10² = 150.0
```

And:

```python
1.5e-3
```

means:

```text
1.5 × 10⁻³ = 0.0015
```

Printing the values:

```python
print(float_1, float_2, float_3)
```

Output:

```text
10.5 150.0 0.0015
```

---

# 🔹 Complex Literals

Complex numbers contain a real and an imaginary component.

Python uses the letter `j` to represent the imaginary part.

```python
# Complex literals

x = 3.14j
```

You can access the imaginary and real parts using:

* `.imag`
* `.real`

```python
print(x, x.imag, x.real)
```

Output:

```text
3.14j 3.14 0.0
```

Since `x` only contains an imaginary component, its real part is `0.0`.

---

# 📝 String Literals

String literals represent textual data.

Python supports multiple ways to write strings.

```python
# ============== String Literals ===============

string = 'This is Python'

strings = "This is Python"

char = "C"

multiline_str = """This is a multiline string with more than one line code."""

unicode = u"\U0001F600\U0001F606\U0001F923"

raw_str = r"raw \n string"

print(string)

print(strings)

print(char)

print(multiline_str)

print(unicode)

print(raw_str)
```

---

## 🔹 Single and Double Quotes

Strings can be created using either:

```python
'This is Python'
```

or:

```python
"This is Python"
```

Both represent strings.

---

## 🔹 Character Literal

Python does not have a separate `char` data type like C or Java.

```python
char = "C"
```

is actually a **string containing one character**.

---

## 🔹 Multiline Strings

Triple quotes can be used to create strings that span multiple lines.

```python
multiline_str = """This is a multiline string
with more than one line."""
```

This is useful when working with larger blocks of text.

---

## 🔹 Unicode Literals

Unicode allows Python to represent characters from different languages and symbols.

```python
unicode = u"\U0001F600\U0001F606\U0001F923"
```

This example represents Unicode emoji characters.

> 📌 In modern Python 3, strings are Unicode by default, so the `u` prefix is generally optional.

---

## 🔹 Raw Strings

A raw string treats backslashes as literal characters in most situations.

```python
raw_str = r"raw \n string"

print(raw_str)
```

Output:

```text
raw \n string
```

Normally, `\n` represents a new line.

However, in a raw string, Python keeps the backslash and `n` as literal characters.

Raw strings are commonly useful when working with:

* File paths
* Regular expressions

---

# ✅ Boolean Literals

Boolean literals represent logical values.

Python has only two Boolean values:

```python
True
False
```

Your example:

```python
# =================== Boolean Literals ================

x = True + 4

y = False + 10

print("a : ", x)

print("b : ", y)
```

Output:

```text
a :  5
b :  10
```

This works because, in Python:

```python
True  → 1
False → 0
```

Therefore:

```text
True + 4  → 1 + 4  → 5

False + 10 → 0 + 10 → 10
```

> 💡 `bool` is closely related to integers in Python, which is why Boolean values can participate in numeric operations.

---

# 🔹 Special Literal

Python provides a special literal called:

```python
None
```

`None` represents the absence of a value.

```python
# ===================== Special Literals ============

z = None

print(z)
```

Output:

```text
None
```

`None` is commonly used when:

* A variable does not currently have a meaningful value.
* A function does not return a value explicitly.
* You want to represent the absence of data.

> 📌 `None` is a special object in Python and is **not the same as `0`, `False`, or an empty string**.

---

# 🧠 Important Notes

* Literals are fixed values written directly in the source code.
* Variables store or reference values represented by literals.
* Python supports numeric, string, Boolean, and special literals.
* Numeric literals can be written in different number systems.
* Python strings can use single, double, or triple quotes.
* Python does not have a separate `char` data type.
* `True` behaves like `1` and `False` behaves like `0` in numeric operations.
* `None` represents the absence of a value.

---

# 🚀 Quick Summary

| Literal Type    | Examples                       |
| --------------- | ------------------------------ |
| Numeric Literal | `10`, `10.5`, `0b1010`, `3+4j` |
| String Literal  | `"Python"`, `'Hello'`          |
| Boolean Literal | `True`, `False`                |
| Special Literal | `None`                         |

---

# 💡 Complete Example

```python
# ================ Numeric Literals =========

a = 0b1010  # Binary literal

b = 100  # Decimal literal

c = 0o310  # Octal literal

d = 0x12c  # Hexadecimal literal


# Float literals

float_1 = 10.5

float_2 = 1.5e2

float_3 = 1.5e-3


# Complex literals

x = 3.14j

print(a, b, c, d)

print(float_1, float_2, float_3)

print(x, x.imag, x.real)


# ============== String Literals ===============

string = 'This is Python'

strings = "This is Python"

char = "C"

multiline_str = """This is a multiline string with more than one line code."""

unicode = u"\U0001F600\U0001F606\U0001F923"

raw_str = r"raw \n string"

print(string)

print(strings)

print(char)

print(multiline_str)

print(unicode)

print(raw_str)


# =================== Boolean Literals ================

x = True + 4

y = False + 10

print("a : ", x)

print("b : ", y)


# ===================== Special Literals ============

z = None

print(z)
```

---

# 🎯 Key Takeaway

> **A literal is a fixed value written directly in your Python code.**

For example:

```python
name = "Kushagra"
age = 21
is_student = True
value = None
```

Here:

* `"Kushagra"` is a **String Literal**
* `21` is a **Numeric Literal**
* `True` is a **Boolean Literal**
* `None` is a **Special Literal**

Understanding literals is important because almost every Python program uses them to represent and work with data.
