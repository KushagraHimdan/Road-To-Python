# Python Important Built-in Functions

Python provides many **built-in functions** that can be used directly without importing a module.

These functions perform common operations such as taking input, converting data types, finding lengths, performing calculations, and inspecting objects.

---

# 1. `print()`

The `print()` function displays output on the screen.

```python id="p7x2km"
print("Hello World")
```

Output:

```text id="8v4k2s"
Hello World
```

---

# 2. `input()`

The `input()` function takes input from the user.

```python id="j4m8qx"
input("Enter your Name : ")
```

By default, `input()` always returns the entered value as a **string**.

---

# 3. `type()`

The `type()` function tells us the data type of an object.

```python id="r5n9wv"
a = 5

type(a)
```

Output:

```text id="m3c7kf"
<class 'int'>
```

To display it using `print()`:

```python
print(type(a))
```

---

# 4. Type Conversion Functions

Python provides functions such as `int()`, `float()`, `str()`, `bool()`, etc. for converting values between compatible data types.

### `int()`

```python id="q8v2lp"
print(int('5'))  # -> 5

print(int(5.9))  # -> 5
```

`int(5.9)` removes the decimal part rather than rounding the number.

```text
5.9 → 5
```

Other common conversion functions:

```python
float("5.5")
str(100)
bool(1)
```

---

# 5. `abs()`

The `abs()` function returns the **absolute value** of a number.

```python id="n6f3tw"
abs(4)   # -> 4

abs(-4)  # -> 4
```

Example:

```python
print(abs(-25))
```

Output:

```text
25
```

---

# 6. `pow()`

The `pow()` function calculates a number raised to a power.

```python id="c4y8hs"
pow(2, 3)   # -> 2^3 = 8

pow(2, -3)  # -> 2^(-3) = 0.125
```

Output:

```text
8
0.125
```

It is similar to:

```python
2 ** 3
```

---

# 7. `min()` and `max()`

### `min()`

Returns the smallest value.

```python id="u7k2qa"
min([2, 5, 0, 1, 7])  # -> 0
```

### `max()`

Returns the largest value.

```python id="f9m4zs"
max([2, 5, 0, 1, 7])  # -> 7
```

They can also work with strings.

```python id="d2p6vx"
print(min("kushagra"))  # -> a

print(max("kushagra"))  # -> u
```

For strings, comparison is based on **Unicode/code-point ordering**, not alphabetical position in every language.

---

# 8. `round()`

The `round()` function rounds a number to a specified number of decimal places.

```python id="h3q8bn"
pi = 22 / 7

print(round(pi, 3))  # -> round to 3 decimal places
```

Output:

```text
3.143
```

Syntax:

```python
round(number, digits)
```

For example:

```python
round(5.6789, 2)
```

gives:

```text
5.68
```

---

# 9. `divmod()`

The `divmod()` function returns the **quotient and remainder** of integer division as a tuple.

```python id="k5w9cr"
t = divmod(5, 2)

print(t)
```

Output:

```text
(2, 1)
```

Because:

```text
5 // 2 = 2
5 % 2  = 1
```

Therefore:

```python
divmod(5, 2)
```

returns:

```python
(5 // 2, 5 % 2)
```

---

# 10. `bin()`, `oct()` and `hex()`

These functions convert an integer into different number systems.

## `bin()`

Converts an integer to **binary**.

```python id="s6h2vm"
a = bin(4)

print(a)
```

Output:

```text
0b100
```

`0b` indicates binary.

---

## `oct()`

Converts an integer to **octal**.

```python id="r8m3yd"
b = oct(16)

print(b)
```

Output:

```text
0o20
```

`0o` indicates octal.

---

## `hex()`

Converts an integer to **hexadecimal**.

```python id="x4p7za"
c = hex(24)

print(c)
```

Output:

```text
0x18
```

`0x` indicates hexadecimal.

---

# 11. `id()`

The `id()` function returns the **identity of an object**.

```python id="v9c3lk"
a = 7

print(id(a))
```

The output is an integer representing the object's identity during its lifetime.

### Important

It is common to describe `id()` as giving the "memory address", but this is an oversimplification.

In CPython, the value commonly corresponds to the object's memory address, but Python's language definition guarantees an **object identity**, not necessarily a physical memory address.

---

# 12. `ord()`

The `ord()` function returns the **Unicode code point** of a single character.

```python id="b7m2qx"
print(ord('K'))
```

Output:

```text
75
```

For example:

```python
print(ord('A'))
print(ord('a'))
```

Output:

```text
65
97
```

The function accepts a string containing exactly **one character**.

---

# 13. `len()`

The `len()` function returns the number of items in an object.

For a string, it returns the number of characters.

```python id="n4k8sp"
print(len("abcdefghijk"))
```

Output:

```text
11
```

It can also be used with collections:

```python
len([1, 2, 3, 4])
```

Output:

```text
4
```

---

# 14. `sum()`

The `sum()` function calculates the total of numeric values in an iterable.

```python id="c8v5mn"
s = sum({2, 4, 5, 6, 8})

print(s)
```

Output:

```text
25
```

It can also be used with lists and tuples:

```python
sum([1, 2, 3, 4])
```

Output:

```text
10
```

---

# 15. `help()`

The `help()` function provides information about Python objects, functions, modules, and other topics.

```python id="z2r6wt"
help("print")
```

This opens Python's built-in documentation/help information for `print`.

You can also use:

```python
help(str)
help(list)
help(len)
```

It is particularly useful when learning Python or exploring an unfamiliar function.

---

# Quick Reference

| Function   | Purpose                | Example            |
| ---------- | ---------------------- | ------------------ |
| `print()`  | Display output         | `print("Hello")`   |
| `input()`  | Take user input        | `input("Name: ")`  |
| `type()`   | Find data type         | `type(5)`          |
| `int()`    | Convert to integer     | `int("5")`         |
| `float()`  | Convert to float       | `float("5.5")`     |
| `str()`    | Convert to string      | `str(5)`           |
| `bool()`   | Convert to Boolean     | `bool(1)`          |
| `abs()`    | Absolute value         | `abs(-5)`          |
| `pow()`    | Calculate power        | `pow(2, 3)`        |
| `min()`    | Find minimum           | `min([2, 5, 1])`   |
| `max()`    | Find maximum           | `max([2, 5, 1])`   |
| `round()`  | Round a number         | `round(3.1415, 2)` |
| `divmod()` | Quotient + remainder   | `divmod(5, 2)`     |
| `bin()`    | Convert to binary      | `bin(4)`           |
| `oct()`    | Convert to octal       | `oct(8)`           |
| `hex()`    | Convert to hexadecimal | `hex(16)`          |
| `id()`     | Get object identity    | `id(a)`            |
| `ord()`    | Get Unicode code point | `ord('A')`         |
| `len()`    | Count items            | `len("Python")`    |
| `sum()`    | Calculate total        | `sum([1, 2, 3])`   |
| `help()`   | Access built-in help   | `help("print")`    |

---

# Important Points

* Built-in functions are available directly in Python.
* Most of them do not require an `import` statement.
* `input()` returns a string by default.
* `type()` can be used to inspect the type of a value.
* `int()` removes the fractional part when converting a positive floating-point value such as `5.9`.
* `min()` and `max()` can work with many iterables.
* `divmod()` returns both quotient and remainder.
* `bin()`, `oct()`, and `hex()` represent integers in different number systems.
* `id()` identifies an object; it should not generally be treated as a portable "memory address".
* `ord()` converts one character into its Unicode code point.
* `len()` counts the number of items in an object.
* `help()` is useful for exploring Python's built-in documentation.

### Remember

> **Built-in functions are ready-made tools provided by Python for common programming tasks.**
