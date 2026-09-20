# Python Tuples

A **tuple** is a built-in Python data type used to store multiple values in a single variable.

Tuples are:

* **Ordered** — elements maintain their position.
* **Immutable** — elements cannot be changed after creation.
* **Heterogeneous** — different data types can be stored together.
* **Indexed** — elements can be accessed using indexes.
* **Allow duplicates** — the same value can appear multiple times.
* **Iterable** — they can be traversed using loops.

Tuples are useful when data should remain **unchanged** after it is created.

---

# 1. Creating a Tuple

An empty tuple can be created using parentheses:

```python
t = ()
```

A tuple can contain multiple values:

```python
t = (1, 2, 3, 4, 5)

print(t)
```

Output:

```text
(1, 2, 3, 4, 5)
```

---

# 2. Homogeneous Tuple

A tuple containing values of the same data type is called a **homogeneous tuple**.

```python
t = (1, 2, 3, 4, 5)

print(t)
```

---

# 3. Heterogeneous Tuple

A tuple can contain values of different data types.

```python
t = (2, "kushagra", True, 9.1)

print(t)
```

Here the tuple contains:

* `int`
* `str`
* `bool`
* `float`

Python tuples can store values of different types just like lists.

---

# 4. Nested Tuples

A tuple can contain another tuple.

## 2D-like Tuple

```python
t = (1, 2, 3, (11, 22))

print(t)
```

Here `(11, 22)` is itself a tuple inside the outer tuple.

---

## Nested / 3D-like Tuple

```python
t = ((1, (2, 3)), (11, 22))

print(t)
```

Tuples can be nested to any required depth.

---

# 5. Single-Element Tuple

A very important property of tuples is that **parentheses alone do not create a tuple**.

```python
t = (1)

print(type(t))
```

Output:

```text
<class 'int'>
```

Python interprets `(1)` as simply the number `1`.

---

## Creating a Single-Element Tuple

A **trailing comma** is required:

```python
t = (1,)

print(t)

print(type(t))
```

Output:

```text
(1,)
<class 'tuple'>
```

The comma is what makes it a tuple.

### Remember

```text
(1)  → int
(1,) → tuple
```

This also works without parentheses:

```python
t = 1,
```

---

# 6. Type Conversion

The `tuple()` function can convert other iterables into tuples.

## String to Tuple

```python
t = tuple("kushagra")

print(t)
```

Output:

```text
('k', 'u', 's', 'h', 'a', 'g', 'r', 'a')
```

Each character becomes an individual tuple element.

---

## List to Tuple

```python
t = tuple([1, 2, 3, 4])

print(t)
```

Output:

```text
(1, 2, 3, 4)
```

### General syntax

```python
tuple(iterable)
```

It creates a new tuple containing the elements of the iterable.

---

# 7. Accessing Tuple Elements

Tuples use **zero-based indexing**, just like lists.

```python
t = (2, "kushagra", True, 9.1)

print(t[1])
```

Output:

```text
kushagra
```

---

## Negative Indexing

Negative indexes access elements from the end.

```python
print(t[-1])
```

Output:

```text
9.1
```

Remember:

```text
Positive indexing → starts from 0
Negative indexing → starts from -1
```

---

# 8. Tuple Slicing

Tuples support slicing.

```python
print(t[:3])
```

Output:

```text
(2, 'kushagra', True)
```

The ending index is excluded.

The general syntax is:

```python
tuple[start:stop:step]
```

For example:

```python
t = (1, 2, 3, 4, 5)

print(t[1:4])
```

Output:

```text
(2, 3, 4)
```

---

# 9. Accessing Nested Tuples

Consider:

```python
t = (1, 2, 3, (11, 22))
```

The nested tuple can be accessed using another index.

```python
print(t[3][-1])
```

Output:

```text
22
```

Here:

```text
t[3]    → (11, 22)
t[3][-1] → 22
```

---

# 10. Tuple vs List

The most important difference between tuples and lists is **mutability**.

| Feature              | List                 | Tuple                         |
| -------------------- | -------------------- | ----------------------------- |
| Syntax               | `[ ]`                | `( )`                         |
| Mutable              | Yes                  | No                            |
| Ordered              | Yes                  | Yes                           |
| Indexed              | Yes                  | Yes                           |
| Heterogeneous        | Yes                  | Yes                           |
| Duplicates           | Allowed              | Allowed                       |
| Can add/remove items | Yes                  | No                            |
| Slicing              | Yes                  | Yes                           |
| Methods              | More                 | Fewer                         |
| Typical use          | Data that may change | Data that should remain fixed |

### Example

A list can be modified:

```python
l = [1, 2, 3]

l[0] = 10
```

But a tuple cannot:

```python
t = (1, 2, 3)

# t[0] = 10
```

The second operation raises a `TypeError`.

---

# 11. Tuples are Immutable

**Immutable** means that the tuple's elements cannot be changed after the tuple has been created.

For example:

```python
t = (1, 2, 3)

# t[0] = 10
```

This is not allowed.

You also cannot directly add or remove elements from a tuple.

Therefore, tuples are often described as **read-only collections**, although "immutable" is the more precise term.

### Important

Immutability applies to the tuple structure itself. If a tuple contains a mutable object such as a list, that nested object may still be modified.

For example:

```python
t = ([1, 2], 3)

t[0].append(4)

print(t)
```

Output:

```text
([1, 2, 4], 3)
```

The tuple still contains the same list object; the list itself was modified.

---

# 12. Deleting a Tuple

Although individual tuple elements cannot be deleted, the **entire tuple variable** can be deleted using `del`.

```python
t = (1, 2, 3, (11, 22))

del t
```

After this, the variable `t` no longer exists.

You cannot do:

```python
# del t[0]
```

because individual tuple elements cannot be deleted.

### Remember

```text
del t      → deletes the tuple variable
del t[0]   → not allowed
```

---

# 13. Tuple Operations

## Concatenation

The `+` operator combines tuples.

```python
t = (1, 2, 3, (11, 22))

t2 = t + t

print(t2)
```

Output:

```text
(1, 2, 3, (11, 22), 1, 2, 3, (11, 22))
```

A new tuple is created.

---

## Repetition

The `*` operator repeats a tuple.

```python
t2 = t * 3

print(t2)
```

Output:

```text
(1, 2, 3, (11, 22), 1, 2, 3, (11, 22), 1, 2, 3, (11, 22))
```

The original tuple is not modified.

---

# 14. Iterating Through a Tuple

A `for` loop can be used to access each element.

```python
t = (1, 2, 3, (11, 22))

for i in t:
    print(i)
```

Output:

```text
1
2
3
(11, 22)
```

Each element is processed one at a time.

---

# 15. Membership Operations

The `in` operator checks whether an element exists in a tuple.

```python
t = (1, 2, 3, (11, 22))

print((11, 22) in t)
```

Output:

```text
True
```

You can also use `not in`:

```python
print(5 not in t)
```

Output:

```text
True
```

Membership checking works with nested values as well.

---

# 16. Built-in Functions with Tuples

Several built-in functions can be used with tuples.

```python
t = (1, 2, 3, 4, 5)

print(len(t))

print(min(t))

print(max(t))

print(sum(t))

print(sorted(t))

print(sorted(t, reverse=True))
```

---

## `len()`

Returns the number of elements.

```text
5
```

---

## `min()`

Returns the smallest element.

```text
1
```

---

## `max()`

Returns the largest element.

```text
5
```

---

## `sum()`

Returns the sum of the numeric elements.

```text
15
```

---

## `sorted()`

Returns the elements in sorted order as a **list**.

```python
print(sorted(t))
```

Output:

```text
[1, 2, 3, 4, 5]
```

Notice that the result is a **list**, not a tuple.

For reverse sorting:

```python
print(sorted(t, reverse=True))
```

Output:

```text
[5, 4, 3, 2, 1]
```

The original tuple remains unchanged.

---

# Tuple Methods

Tuples have fewer methods than lists because they are immutable.

The two important tuple-specific methods are:

| Method    | Purpose                                   |
| --------- | ----------------------------------------- |
| `count()` | Counts occurrences of a value             |
| `index()` | Returns the index of the first occurrence |

Example:

```python
t = (1, 2, 2, 3, 2)

print(t.count(2))
print(t.index(3))
```

Output:

```text
3
3
```

---

# Why Use Tuples?

Tuples are useful when the collection of values should not be changed.

Common examples include:

```python
coordinates = (28.61, 77.20)
```

```python
rgb = (255, 255, 255)
```

```python
student = ("Kushagra", 21, "CSE")
```

They can also be used to return multiple values from a function.

```python
def get_data():
    return "Kushagra", 21
```

The returned values form a tuple:

```python
data = get_data()

print(data)
```

Output:

```text
('Kushagra', 21)
```

---

# Quick Reference

| Operation         | Example         |
| ----------------- | --------------- |
| Create            | `t = (1, 2, 3)` |
| Empty tuple       | `t = ()`        |
| Single tuple      | `t = (1,)`      |
| Indexing          | `t[0]`          |
| Negative indexing | `t[-1]`         |
| Slicing           | `t[1:4]`        |
| Concatenation     | `t1 + t2`       |
| Repetition        | `t * 3`         |
| Membership        | `x in t`        |
| Length            | `len(t)`        |
| Minimum           | `min(t)`        |
| Maximum           | `max(t)`        |
| Sum               | `sum(t)`        |
| Sorting           | `sorted(t)`     |
| Count             | `t.count(x)`    |
| Find index        | `t.index(x)`    |
| Delete tuple      | `del t`         |

---

# Important Points to Remember

* A tuple is an **ordered and immutable** collection.
* Tuples can store different data types.
* Tuples support indexing and slicing.
* A tuple can contain other tuples or lists.
* `(1)` is an `int`, while `(1,)` is a tuple.
* The comma is what creates a single-element tuple.
* `tuple()` can convert an iterable into a tuple.
* You cannot directly add, remove, or modify tuple elements.
* `+` concatenates tuples.
* `*` repeats tuples.
* `in` and `not in` perform membership checks.
* `sorted()` returns a **list**, even when the input is a tuple.
* Tuples have only two dedicated methods: `count()` and `index()`.
* `del t` deletes the tuple variable, but individual elements cannot be deleted.

### One-line memory trick

```text
Tuple → Ordered + Indexed + Immutable

Create  → ()
Access  → index / slice
Combine → +
Repeat  → *
Search  → in / index
Count   → count()
Delete  → del tuple
Sort    → sorted()
```
