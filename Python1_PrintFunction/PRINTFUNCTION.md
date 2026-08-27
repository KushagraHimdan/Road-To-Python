# Python `print()` Function

The `print()` function is one of the most commonly used functions in Python. It is used to display output on the screen.

## 1. Printing a String

Strings are written inside quotation marks (`"` or `'`).

```python
print("Hello World")
```

**Output:**

```text
Hello World
```

---

## 2. Printing an Integer

Integers are whole numbers without a decimal point.

```python
print(5)
```

**Output:**

```text
5
```

---

## 3. Printing a Floating-Point Number

Numbers containing a decimal point are called **floating-point numbers**.

```python
print(2.7)
```

**Output:**

```text
2.7
```

> Note: In Python, `2.7` is a `float`, not a `double` as in some other programming languages.

---

## 4. Printing a Boolean

Boolean values can be either `True` or `False`.

```python
print(False)
```

**Output:**

```text
False
```

Remember that Python is **case-sensitive**, so `True` and `False` must start with a capital letter.

---

## 5. Printing Multiple Values Together

The `print()` function can display multiple values by separating them with commas.

```python
print("Apple", "Orange", "Mango", "Kiwi")
```

**Output:**

```text
Apple Orange Mango Kiwi
```

Different data types can also be printed together:

```python
print("Apple", 3, True, "Kiwi")
```

**Output:**

```text
Apple 3 True Kiwi
```

By default, Python places a **space** between values.

---

## 6. Using the `sep` Parameter

The `sep` parameter specifies what should be placed **between multiple values**.

```python
print("Apple", "Orange", "Mango", "Kiwi", sep='/')
```

**Output:**

```text
Apple/Orange/Mango/Kiwi
```

You can use any string as the separator:

```python
print("2026", "08", "25", sep="-")
```

**Output:**

```text
2026-08-25
```

The default value of `sep` is a space (`" "`).

---

## 7. Using the `end` Parameter

The `end` parameter specifies what Python should print **at the end** of the output.

By default, `print()` adds a newline (`\n`) after printing.

```python
print("Apple")
print("Orange")
```

**Output:**

```text
Apple
Orange
```

We can change this behavior using `end`:

```python
print("Apple", end=" ")
print("Orange")
```

**Output:**

```text
Apple Orange
```

Another example:

```python
print("Apple", end="/")
print("Orange")
```

**Output:**

```text
Apple/Orange
```

---

## 8. `sep` and `end` Together

Both parameters can be used at the same time.

```python
print("Apple", "Orange", "Mango", sep=" | ", end=".")
```

**Output:**

```text
Apple | Orange | Mango.
```

---

## Quick Reference

| Feature         | Example                    | Purpose                       |
| --------------- | -------------------------- | ----------------------------- |
| Basic print     | `print("Hello")`           | Displays output               |
| Multiple values | `print("A", "B")`          | Prints multiple values        |
| `sep`           | `print("A", "B", sep="-")` | Changes separator             |
| `end`           | `print("A", end="!")`      | Changes what comes at the end |
| New line        | `print("A\nB")`            | Moves output to a new line    |

### Important Points :

* `print()` is used to display information on the screen.
* Strings require quotation marks.
* Integers and floats do not require quotation marks.
* Boolean values are written as `True` and `False`.
* Multiple values can be passed to `print()` using commas.
* `sep` controls the separator **between** values.
* `end` controls what is printed **after** the values.
* By default, `sep=" "` and `end="\n"`.
