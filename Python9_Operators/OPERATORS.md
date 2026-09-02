# Python Operators 

## 📌 Introduction

**Operators** are special symbols or keywords used to perform operations on variables and values.

Python provides several types of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Identity Operators
7. Membership Operators

---

# 🔹 Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

```python
# =================== Arithmetic operation =============

a = 5
b = 2

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulo
print(a ** b)  # Power
print(a // b)  # Integer/Floor Division
```

### Output

```text
7
3
10
2.5
1
25
2
```

---

## 📊 Arithmetic Operators Summary

| Operator | Name           | Example  | Result |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 2`  | `7`    |
| `-`      | Subtraction    | `5 - 2`  | `3`    |
| `*`      | Multiplication | `5 * 2`  | `10`   |
| `/`      | Division       | `5 / 2`  | `2.5`  |
| `%`      | Modulo         | `5 % 2`  | `1`    |
| `**`     | Exponentiation | `5 ** 2` | `25`   |
| `//`     | Floor Division | `5 // 2` | `2`    |

### 📌 Modulo Operator

The modulo operator `%` returns the remainder.

```python
print(5 % 2)
```

Output:

```text
1
```

---

# 🔹 Comparison Operators

Comparison operators are used to compare two values.

The result of a comparison is always a Boolean value:

```python
True
```

or:

```python
False
```

```python
# ==================== Comparison operation ==============

print(a > b)

print(a < b)

print(a >= b)

print(a <= b)

print(a == b)

print(a != b)
```

### Output

```text
True
False
True
False
False
True
```

---

## 📊 Comparison Operators Summary

| Operator | Meaning                  |
| -------- | ------------------------ |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |

> 📌 `=` is used for assignment, while `==` is used for comparison.

---

# 🔹 Logical Operators

Logical operators are used to combine or modify Boolean expressions.

Python provides three logical operators:

* `or`
* `and`
* `not`

```python
# ===================== Logical operation ===============

x = True

y = False

print(x or y)

print(x and y)

print(not x)

print(not y)
```

### Output

```text
True
False
False
True
```

---

## 📊 Logical Operators Summary

| Operator | Description                                        |
| -------- | -------------------------------------------------- |
| `and`    | Returns `True` when both conditions are true       |
| `or`     | Returns `True` when at least one condition is true |
| `not`    | Reverses the Boolean value                         |

### Example

```python
True and False
```

Result:

```text
False
```

```python
True or False
```

Result:

```text
True
```

---

# 🔹 Bitwise Operators

Bitwise operators perform operations on the binary representation of numbers.

```python
# ================== Bitwise operation =============

m = 2

n = 3

print(m & n)

print(m | n)

print(m >> 2)

print(n << 2)

print(~m)
```

### Output

```text
2
3
0
12
-3
```

---

## 📊 Bitwise Operators Summary

| Operator | Name        |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left Shift  |            |
| `>>`     | Right Shift |            |

### Example

```text
2 → 10
3 → 11
```

Bitwise AND:

```text
10
11
--
10 → 2
```

Therefore:

```python
2 & 3
```

returns:

```text
2
```

---

# 🔹 Assignment Operators

Assignment operators are used to assign values to variables.

Python also provides compound assignment operators.

```python
# ========= Assignment operation ================

k = 3

print(k)

k += 4

print(k)

k -= 2

print(k)

k *= 3

print(k)

k &= 2

print(k)
```

### Step-by-Step Result

```text
3
7
5
15
2
```

---

## 📊 Assignment Operators Summary

| Operator | Example   | Equivalent To |      |        |    |
| -------- | --------- | ------------- | ---- | ------ | -- |
| `=`      | `a = 5`   | Assign value  |      |        |    |
| `+=`     | `a += 5`  | `a = a + 5`   |      |        |    |
| `-=`     | `a -= 5`  | `a = a - 5`   |      |        |    |
| `*=`     | `a *= 5`  | `a = a * 5`   |      |        |    |
| `/=`     | `a /= 5`  | `a = a / 5`   |      |        |    |
| `%=`     | `a %= 5`  | `a = a % 5`   |      |        |    |
| `**=`    | `a **= 5` | `a = a ** 5`  |      |        |    |
| `//=`    | `a //= 5` | `a = a // 5`  |      |        |    |
| `&=`     | `a &= 5`  | `a = a & 5`   |      |        |    |
| `        | =`        | `a            | = 5` | `a = a | 5` |

---

# 🚫 Increment and Decrement Operators

Python does not have traditional pre-increment or post-increment operators such as:

```text
++k
k++
```

These are commonly found in languages such as C, C++, and Java.

In Python, you can write:

```python
k += 1
```

Similarly, for decrementing:

```python
k -= 1
```

---

# 🔹 Identity Operators

Identity operators are used to check whether two variables refer to the **same object**.

Python provides:

* `is`
* `is not`

```python
# ============== Identity operators =============

# Check if two variables refer to the same object

p = 5
q = 5

print(p is q)

p = "Hello"
q = "Hello"

print(p is q)

p = [1, 2, 3]
q = [1, 2, 3]

print(p is q)

p = "Hello-world"
q = "Hello-world"

print(p is not q)
```

For the list example:

```python
p = [1, 2, 3]
q = [1, 2, 3]
```

Both lists contain the same values, but they are different objects.

Therefore:

```python
p is q
```

returns:

```text
False
```

However:

```python
p == q
```

returns:

```text
True
```

because `==` compares **values**, while `is` compares **object identity**.

> ⚠️ **Important:** Do not use `is` as a replacement for `==`. Whether two immutable values such as strings or integers refer to the same object can depend on Python's implementation and optimizations.

A common and recommended use of `is` is:

```python
value = None

if value is None:
    print("No value")
```

---

# 🔹 Membership Operators

Membership operators are used to check whether a value exists inside a collection.

Python provides:

* `in`
* `not in`

```python
# ============= Membership operator ================

h = "Delhi"

print("D" in h)

print("D" not in h)

h = [1, 2, 3]

print(1 in h)

print(5 in h)
```

### Output

```text
True
False
True
False
```

---

## 📌 Membership Operators Can Be Used With

Membership operators are commonly used with:

* Strings
* Lists
* Tuples
* Sets
* Dictionaries

### Example

```python
numbers = [1, 2, 3, 4]

print(2 in numbers)
```

Output:

```text
True
```

---

# 🧠 Important Notes

* Arithmetic operators perform mathematical calculations.
* Comparison operators compare values and return `True` or `False`.
* Logical operators work with Boolean expressions.
* Bitwise operators work with binary representations of numbers.
* Assignment operators assign or update variable values.
* Python does not support `++` or `--`.
* Identity operators compare object identity.
* Membership operators check whether a value exists inside a collection.

---

# 🚀 Quick Summary

| Operator Category | Operators                           |
| ----------------- | ----------------------------------- |
| Arithmetic        | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| Comparison        | `>`, `<`, `>=`, `<=`, `==`, `!=`    |
| Logical           | `and`, `or`, `not`                  |
| Bitwise           | `&`, `\|`, `^`, `~`, `<<`, `>>`     |
| Assignment        | `=`, `+=`, `-=`, `*=`, etc.         |
| Identity          | `is`, `is not`                      |
| Membership        | `in`, `not in`                      |

---

# 🎯 Key Takeaway

Operators allow Python programs to perform calculations, comparisons, logical decisions, binary operations, assignments, identity checks, and membership checks.

A very important distinction to remember is:

```python
==  # Compares values

is  # Compares object identity
```

And for membership:

```python
in      # Checks whether something exists

not in  # Checks whether something does not exist
```

Understanding operators is essential because they are used throughout Python—from simple mathematical calculations to complex conditional statements and program logic.
