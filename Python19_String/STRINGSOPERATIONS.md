# Python Strings

## What is a String?

A **string** is a sequence of characters.

In Python, strings are sequences of **Unicode characters**, which means they can represent text from many writing systems and symbols.

Examples:

```python
"Kushagra"
"Hello World"
"12345"
"Python @ 2026"
```

A string can contain:

* Letters
* Numbers
* Spaces
* Special characters
* Unicode characters

---

# Creating Strings

Python allows strings to be created using:

* Single quotes `' '`
* Double quotes `" "`
* Triple single quotes `''' '''`
* Triple double quotes `""" """`

### Examples

```python
str = 'Kushagra'

print(str)

str = "It's good outside!!"

print(str)

str = '''Let's Play'''

print(str)
```

Output:

```text
Kushagra
It's good outside!!
Let's Play
```

### Why Different Quotes?

Different quote styles can make it easier to include quotation marks inside a string.

For example:

```python
str = "It's good outside!!"
```

The apostrophe in `It's` does not terminate the string because the string is surrounded by double quotes.

---

# Important Note About `str`

In the examples above:

```python
str = "Kushagra"
```

`str` is being used as a variable name.

However, `str` is also the name of Python's built-in string conversion function:

```python
str(100)
```

Therefore, it is generally better to use a name such as:

```python
name = "Kushagra"
```

instead of:

```python
str = "Kushagra"
```

This avoids **shadowing** the built-in `str()` function.

---

# Accessing Characters from a String

Since a string is a sequence, individual characters can be accessed using **indexing**.

```python
str = "Kushagra"

print(str[4])
```

Output:

```text
a
```

Python uses **zero-based indexing**, meaning the first character is at index `0`.

---

# Positive Indexing

Positive indexing starts from the beginning of the string.

For:

```python
str = "Kushagra"
```

the indexes are:

```text
 K  u  s  h  a  g  r  a
 0  1  2  3  4  5  6  7
```

Therefore:

```python
print(str[7])
```

Output:

```text
a
```

---

# Negative Indexing

Negative indexing starts from the end of the string.

```text
 K  u  s  h  a  g  r  a
-8 -7 -6 -5 -4 -3 -2 -1
```

Therefore:

```python
print(str[-1])
```

Output:

```text
a
```

`-1` always represents the **last character**.

---

# String Indexing Summary

For:

```python
str = "Kushagra"
```

| Character | Positive Index | Negative Index |
| --------- | -------------: | -------------: |
| `K`       |            `0` |           `-8` |
| `u`       |            `1` |           `-7` |
| `s`       |            `2` |           `-6` |
| `h`       |            `3` |           `-5` |
| `a`       |            `4` |           `-4` |
| `g`       |            `5` |           `-3` |
| `r`       |            `6` |           `-2` |
| `a`       |            `7` |           `-1` |

---

# String Slicing

**Slicing** is used to extract a portion of a string.

### Syntax

```python
string[start:stop:step]
```

* `start` → starting index
* `stop` → ending index, **not included**
* `step` → number of positions to move

---

## Basic Slicing

```python
str = "Hello World"

print(str[0:5])

print(str[2:])

print(str[:5])
```

Output:

```text
Hello
llo World
Hello
```

### `str[0:5]`

Starts at index `0` and stops before index `5`.

```text
H e l l o
0 1 2 3 4
```

So the result is:

```text
Hello
```

### `str[2:]`

Starts from index `2` and goes until the end.

```text
llo World
```

### `str[:5]`

Starts from the beginning and stops before index `5`.

```text
Hello
```

---

# Slicing with Step

```python
print(str[0:5:2])
```

Output:

```text
Hlo
```

The step is `2`, so Python takes every second character.

---

### Negative Index Slicing

```python
print(str[-5:-1:2])
```

This uses negative indexes and a positive step.

The selected characters are taken from left to right according to the specified slice.

---

# Negative Step

A negative step moves through the string **backwards**.

```python
print(str[::-1])
```

Output:

```text
dlroW olleH
```

This is a common way to reverse a string.

---

Another example:

```python
print(str[-1:-5:-1])
```

This starts at the last character and moves backwards.

---

### Important Slicing Rule

```python
str[-5:-1:-2]
```

does not produce the expected reverse slice because the start and stop positions do not align with the direction of a negative step.

When using a **negative step**, the slice should generally move from a higher index toward a lower index.

For example:

```python
str[5:1:-1]
```

moves backwards from index `5` toward index `2`.

---

# Editing and Deleting Strings

## Strings are Immutable

Python strings are **immutable**.

This means that once a string object is created, its individual characters cannot be changed.

For example, this is not allowed:

```python
str = "Hello"
str[0] = "J"
```

It produces an error because strings cannot be modified character-by-character.

Instead, create a new string:

```python
str = "Hello"
str = "J" + str[1:]

print(str)
```

Output:

```text
Jello
```

---

## Deleting a String Variable

Your example:

```python
str = "Nice Food"

del str

print(str)
```

After:

```python
del str
```

the variable `str` is deleted from the current namespace.

Therefore, attempting:

```python
print(str)
```

will result in a `NameError` because the variable no longer exists.

### Important Distinction

* **Immutable** → the string object's contents cannot be changed.
* `del` → removes the variable binding.

`del` does not mean that you manually erase the string's memory.

---

# String Operations

Python supports several operations on strings.

---

## 1. Arithmetic-like Operations

### String Concatenation

The `+` operator joins strings together.

```python
str = "Kushagra"

str2 = str + "!!"

print(str2)
```

Output:

```text
Kushagra!!
```

This is called **concatenation**.

---

### String Repetition

The `*` operator can repeat a string.

```python
str3 = str2 * 20

print(str3)
```

The string is repeated 20 times.

For example:

```python
"Hi " * 3
```

produces:

```text
Hi Hi Hi
```

---

# 2. Relational Operations

Strings can be compared using comparison operators.

```python
str = "Kushagra"

b = (str == str2)

print(b)

b = (str != str2)

print(b)
```

The operators include:

```text
==
!=
<
>
<=
>=
```

---

## Lexicographical Comparison

Strings are compared **lexicographically**, based on the Unicode code points of their characters.

```python
b = ("Kushagra" > "Lion")

print(b)
```

Python compares the strings character by character.

The first characters are:

```text
K < L
```

so the result is:

```text
False
```

Another example:

```python
b = ("lion" > "Lion")

print(b)
```

The lowercase and uppercase characters have different Unicode code points.

For example:

```python
ord('L')  # 76
ord('l')  # 108
```

Therefore:

```text
"lion" > "Lion"
```

is:

```text
True
```

---

# 3. Logical Operations with Strings

Strings can also be used with `and`, `or`, and `not`.

Python treats strings according to their **truth value**.

### Empty String

```python
""
```

is considered **False**.

### Non-empty String

```python
"kushagra"
```

is considered **True**.

---

## `not`

```python
b = not "hello"

print(b)

b = not ""

print(b)
```

Output:

```text
False
True
```

Because:

```text
"hello" → True → not True → False
""      → False → not False → True
```

---

## `and`

```python
b = '' and "hello"

print(b)
```

Output:

```text
```

An empty string is falsy, so `and` returns the falsy operand.

Another example:

```python
b = 'world' and "hello"

print(b)
```

Output:

```text
hello
```

Both operands are truthy, so `and` returns the second operand.

---

## `or`

```python
b = '' or "hello"

print(b)
```

Output:

```text
hello
```

The first operand is falsy, so `or` returns the second operand.

```python
b = 'world' or "hello"

print(b)
```

Output:

```text
world
```

The first operand is already truthy, so `or` returns it.

### Important

`and` and `or` do not necessarily return `True` or `False`.

They can return one of their operands.

---

# 4. Looping Through a String

Because strings are sequences, a `for` loop can iterate through their characters.

```python
f = "Hello Kushagra"

for i in f:

    print(i, end=" ")

print()
```

Output:

```text
H e l l o   K u s h a g r a
```

Each iteration gives one character.

For example:

```text
i = H
i = e
i = l
i = l
...
```

---

# 5. Membership Operations

The `in` and `not in` operators check whether a character or substring exists inside a string.

```python
m = "kushagra"

k = ("u" in m)

print(k)

k = ("K" in m)

print(k)

k = ("Z" not in m)

print(k)
```

Output:

```text
True
False
True
```

### Why?

```text
"u" → exists in "kushagra" → True
"K" → does not exist because strings are case-sensitive → False
"Z" → does not exist → True for "not in"
```

---

# Strings are Case-Sensitive

Python treats uppercase and lowercase characters as different.

```python
"K" != "k"
```

Therefore:

```python
"K" in "kushagra"
```

is:

```text
False
```

while:

```python
"k" in "kushagra"
```

is:

```text
True
```

---

# Complete Example

```python
# ================= Strings ============

# Strings are sequence of characters

# In Python specifically string are a sequence of unicode characters

# creating Strings

str = 'Kushagra'

print(str)

str = "It's good outside!!"

print(str)

str = '''Let's Play'''

print(str)

# Accessing substring from a string

# indexing

str = "Kushagra"

print(str[4])

# positive indexing

print(str[7])

# negative indexing

print(str[-1])

# slicing

str = "Hello World"

print(str[0:5])

print(str[2:])

print(str[:5])

# steps

print(str[0:5:2])

print(str[-5:-1:2])

# print(str[-5:-1:-2]) -> invalid direction for this slice

print(str[::-1])

print(str[-1:-5:-1])

# Editing and Deleting in Strings

str = "Nice Food"  # String are immutable

del str

# print(str) -> NameError because the variable was deleted

# ================ String operations ==============

str = "Kushagra"

# arithmetic operations

str2 = str + "!!"

print(str2)

str3 = str2 * 20

print(str3)

# relational operations

b = (str == str2)

print(b)

b = (str != str2)

print(b)

b = ("Kushagra" > "Lion")  # lexicographically comparable

print(b)

b = ("lion" > "Lion")  # Unicode code point comparison

print(b)

# logical operations

# "" -> false (empty = false)

# "kushagra" -> true (non empty = true)

b = not "hello"

print(b)

b = not ""

print(b)

b = '' and "hello"

print(b)

b = '' or "hello"

print(b)

b = 'world' and "hello"

print(b)

b = 'world' or "hello"

print(b)

# loops

f = "Hello Kushagra"

for i in f:

    print(i, end=" ")

print()

# membership operations

m = "kushagra"

k = ("u" in m)

print(k)

k = ("K" in m)

print(k)

k = ("Z" not in m)

print(k)
```

---

# Quick Reference

| Concept           | Example        | Purpose                  |
| ----------------- | -------------- | ------------------------ |
| Create string     | `"Hello"`      | Store text               |
| Indexing          | `str[2]`       | Access one character     |
| Negative indexing | `str[-1]`      | Access from the end      |
| Slicing           | `str[1:5]`     | Extract part of a string |
| Step              | `str[::2]`     | Skip characters          |
| Reverse           | `str[::-1]`    | Reverse a string         |
| Concatenation     | `"Hi" + "!"`   | Join strings             |
| Repetition        | `"Hi" * 3`     | Repeat a string          |
| Comparison        | `"a" < "b"`    | Compare strings          |
| Membership        | `"a" in str`   | Check for presence       |
| Iteration         | `for i in str` | Visit each character     |
| Length            | `len(str)`     | Count characters         |

---

# Key Takeaways

* A string is a **sequence of Unicode characters**.
* Python supports single, double, and triple-quoted strings.
* Strings use **zero-based indexing**.
* Negative indexing starts from `-1` at the end.
* Slicing uses `start:stop:step`.
* The `stop` index is excluded.
* A negative step moves through the string backwards.
* Strings are **immutable**.
* `+` concatenates strings and `*` repeats them.
* String comparisons are lexicographical and based on Unicode code points.
* Empty strings are **falsy**; non-empty strings are **truthy**.
* `and` and `or` can return operands rather than only `True` or `False`.
* Strings can be iterated character by character using a `for` loop.
* `in` and `not in` are used for membership checking.
* String comparisons and membership checks are **case-sensitive**.

### Remember

> **String → Sequence → Index → Slice → Operate → Iterate**
