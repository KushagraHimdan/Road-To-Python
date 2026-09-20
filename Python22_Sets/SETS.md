# Python Sets

A **set** is a built-in Python data type used to store a collection of **unique elements**.

Sets are:

* **Unordered** — elements do not have a guaranteed positional order.
* **Mutable** — elements can be added or removed.
* **Unique** — duplicate elements are automatically removed.
* **Unindexed** — elements cannot be accessed using indexes.
* **Iterable** — elements can be accessed using a loop.
* **Heterogeneous** — different compatible data types can be stored together.

Sets are especially useful for **removing duplicates** and performing mathematical set operations such as union, intersection, and difference.

---

# 1. Rules of Sets

## Rule 1: Sets Do Not Allow Duplicates

A set stores each value only once.

```python id="7i3xq1"
s = {1, 1, 2, 3, 3, 4, 5, 5}

print(s)
```

Output:

```text id="5h2l7v"
{1, 2, 3, 4, 5}
```

All duplicate values are automatically removed.

---

## Rule 2: Sets Do Not Support Indexing or Slicing

Sets do not have positions like lists or tuples.

Therefore, this is not allowed:

```python id="g6k8f2"
# print(s[0])
```

It raises a `TypeError` because a set does not support indexing.

Similarly, slicing is not supported:

```python id="4d7p8m"
# s[1:3]
```

---

## Rule 3: Sets Do Not Allow Mutable Elements

Set elements must be **hashable**.

Mutable objects such as lists, dictionaries, and other sets are not hashable and therefore cannot normally be stored directly inside a set.

For example:

```python id="m8j4s2"
# s = {[1, 2, 3], "Kushagra"}
```

This raises a `TypeError` because a list is mutable.

However, an immutable tuple can be stored:

```python id="3f9q1k"
s = {(1, 2, 3), "Kushagra"}

print(s)
```

A tuple can be an element of a set when all of its elements are themselves hashable.

---

## Rule 4: Sets Themselves Are Mutable

Although set elements must be hashable, the set itself can be changed.

For example:

```python id="1z8c6v"
s = {1, 2, 3}

s.add(4)

print(s)
```

The set has been modified.

This gives an important distinction:

```text
Set → Mutable
Set elements → Must be hashable
```

---

# 2. Creating a Set

## Empty Set

An empty set is created using `set()`:

```python id="r7k4p3"
s = set()

print(s)

print(type(s))
```

Output:

```text id="0r8m1x"
set()
<class 'set'>
```

### Important

Do not use `{}` for an empty set.

```python id="9m2w5h"
s = {}
```

This creates an empty **dictionary**, not a set.

```text
{}       → dictionary
set()    → empty set
```

---

# 3. Homogeneous Set

A set containing elements of the same data type is called a homogeneous set.

```python id="6k1p8v"
s = {1, 2, 3, 4}

print(s)
```

---

# 4. Heterogeneous Set

A set can contain elements of different data types, provided those elements are hashable.

```python id="2x5q9a"
s = {1, 2.2, "True", "Kushagra"}

print(s)
```

The set contains:

* `int`
* `float`
* `str`

---

# 5. Duplicate Elements

Sets automatically eliminate duplicate values.

```python id="w4j7n2"
s = {1, 1, 2, 3, 3, 4, 5, 5}

print(s)
```

Conceptually, Python stores:

```text
{1, 2, 3, 4, 5}
```

This makes sets very useful when you need to remove duplicates from a collection.

---

# 6. Sets and Ordering

Sets do not provide a positional ordering that you can rely on.

The order in which elements appear when printing or iterating over a set may differ from the order in which they were written.

```python id="q6c9y3"
s = {5, 2, 8, 1, 4}

print(s)
```

The displayed order should **not** be treated as meaningful.

Sets are implemented using **hashing**, which allows efficient membership checking.

### Important

Do not rely on the printed order of a set.

If you need a specific order, use a list or sort the set:

```python id="p1r8k4"
print(sorted(s))
```

---

# 7. Sets Do Not Support Indexing

Consider:

```python id="v2m6x9"
s = {1, 1, 2, 3, 3, 4, 5, 5}
```

This is invalid:

```python id="7b3n5q"
# print(s[0])
```

A set has no positional index.

If you need to access elements individually, you can iterate over the set:

```python id="n8q2k6"
for i in s:
    print(i)
```

---

# 8. Adding Items

## `add()`

The `add()` method adds a single element to a set.

```python id="4v7p2m"
s = {1, 1, 2, 3, 3, 4, 5, 5}

s.add(8)

print(s)
```

Output will contain:

```text
8
```

If you add an element that already exists, the set remains unchanged.

```python id="0x5k9r"
s.add(8)
```

Adding `8` again does not create a duplicate.

---

# 9. Deleting Items

Python provides several ways to remove elements from a set.

---

## `del`

`del` can delete the entire set variable.

```python id="c4m8y1"
s = {1, 1, 2, 3, 3, 4, 5, 5}

del s
```

After this, the variable `s` no longer exists.

`del` is not used to remove a particular set element by index because sets do not support indexing.

---

## `remove()`

`remove()` removes a specified element.

```python id="e7q3t5"
s = {1, 1, 2, 3, 3, 4, 5, 5}

s.remove(5)

print(s)
```

The value `5` is removed.

### Important

If the specified element does not exist, `remove()` raises a `KeyError`.

---

## `pop()`

`pop()` removes and returns **an arbitrary element** from the set.

```python id="h2v8c4"
s = {1, 1, 2, 3, 3, 4, 5, 5}

s.pop()

print(s)
```

### Important correction

You commented:

```text
because of hashing 1 will be removed
```

You should **not assume that `1` will always be removed**.

`set.pop()` removes an arbitrary element. The specific element should not be relied upon.

---

## `clear()`

`clear()` removes all elements from the set.

```python id="j5n1r7"
s = {1, 2, 3, 4, 5}

s.clear()

print(s)
```

Output:

```text
set()
```

The set still exists; it is simply empty.

---

# 10. Iterating Through a Set

A `for` loop can be used to iterate through the elements.

```python id="f8w3k6"
s = {1, 2, 3, 4, 5}

for i in s:
    print(i)
```

The elements are processed one at a time.

However, do not rely on the iteration order.

---

# 11. Membership Operations

The `in` operator checks whether an element exists in a set.

```python id="r4m7v2"
print(1 in s)
```

Output:

```text
True
```

You can also use `not in`:

```python id="y6p2c8"
print(10 not in s)
```

Set membership testing is one of the major reasons sets are useful.

---

# 12. Built-in Functions

Several built-in functions work with sets.

```python id="x9q4m1"
s = {1, 2, 3, 4, 5}

print(len(s))

print(min(s))

print(max(s))

print(sum(s))
```

### `len()`

Returns the number of elements.

```text
5
```

### `min()`

Returns the smallest element.

```text
1
```

### `max()`

Returns the largest element.

```text
5
```

### `sum()`

Returns the sum of numeric elements.

```text
15
```

---

# 13. `sorted()`

`sorted()` returns the elements of a set in sorted order as a **list**.

```python id="u3k8p5"
s = {1, 2, 3, 4, 5}

print(sorted(s))

print(sorted(s, reverse=True))
```

Output:

```text
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
```

### Important

`sorted()` does not convert the set itself into a sorted set.

It returns a **list**.

```python id="b7m2x9"
result = sorted(s)

print(type(result))
```

Output:

```text
<class 'list'>
```

---

# 14. Set Operations

One of the most powerful features of sets is their support for mathematical set operations.

Consider:

```python id="q8v4n6"
s1 = {1, 2, 4, 6, 9, 7}

s2 = {2, 3, 5, 10, 1, 8}
```

---

## `union()`

`union()` returns all unique elements from both sets.

```python id="m5r1x8"
print(s1.union(s2))
```

Conceptually:

```text
s1 ∪ s2
```

Result:

```text
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

### Meaning

```text
Union → Everything from both sets
```

---

## `intersection()`

`intersection()` returns only the elements common to both sets.

```python id="k3w7p2"
print(s1.intersection(s2))
```

Here the common elements are:

```text
{1, 2}
```

### Meaning

```text
Intersection → Common elements
```

---

## `difference()`

`difference()` returns elements that exist in the first set but **not** in the second set.

```python id="z6n2q4"
print(s1.difference(s2))
```

This means:

```text
s1 - s2
```

Result:

```text
{4, 6, 7, 9}
```

For the reverse direction:

```python id="t8v5m1"
print(s2.difference(s1))
```

Result:

```text
{3, 5, 8, 10}
```

### Important

Difference is **directional**.

```text
s1 - s2 ≠ s2 - s1
```

---

## `symmetric_difference()`

`symmetric_difference()` returns elements that belong to **either set but not both**.

```python id="n4y7c2"
print(s1.symmetric_difference(s2))
```

The common elements `1` and `2` are excluded.

Conceptually:

```text
(A ∪ B) - (A ∩ B)
```

### Meaning

```text
Symmetric Difference → Elements that are not common
```

---

# 15. `isdisjoint()`

`isdisjoint()` checks whether two sets have **no elements in common**.

```python id="p8m3x6"
print(s1.isdisjoint(s2))
```

Since `s1` and `s2` contain `1` and `2` in common:

```text
False
```

If two sets had no common elements, it would return:

```text
True
```

---

# 16. `issubset()`

`issubset()` checks whether every element of one set exists inside another set.

```python id="v5q1n9"
print(s1.issubset(s2))
```

This returns `False` because all elements of `s1` are not present in `s2`.

### Example

```python id="c7k2r4"
a = {1, 2}

b = {1, 2, 3, 4}

print(a.issubset(b))
```

Output:

```text
True
```

Because every element of `a` exists in `b`.

---

# 17. Related Set Methods

There are a few other useful methods worth remembering.

## `issuperset()`

Checks whether a set contains every element of another set.

```python id="w2m8p5"
a = {1, 2, 3, 4}

b = {1, 2}

print(a.issuperset(b))
```

Output:

```text
True
```

---

## `discard()`

`discard()` removes an element if it exists.

Unlike `remove()`, it does **not raise an error** if the element is absent.

```python id="e4q9n7"
s = {1, 2, 3}

s.discard(5)

print(s)
```

The set remains unchanged.

### `remove()` vs `discard()`

| Method       | Element exists | Element absent    |
| ------------ | -------------- | ----------------- |
| `remove(x)`  | Removes it     | Raises `KeyError` |
| `discard(x)` | Removes it     | Does nothing      |

---

# Set Operations Quick Reference

For:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

| Operation            | Meaning                     | Example                     |
| -------------------- | --------------------------- | --------------------------- |
| Union                | All elements                | `A.union(B)`                |
| Intersection         | Common elements             | `A.intersection(B)`         |
| Difference           | In A but not B              | `A.difference(B)`           |
| Symmetric difference | In either, but not both     | `A.symmetric_difference(B)` |
| Subset               | A completely contained in B | `A.issubset(B)`             |
| Superset             | A contains B                | `A.issuperset(B)`           |
| Disjoint             | No common elements          | `A.isdisjoint(B)`           |

The operator versions are also available:

```python
A | B    # Union
A & B    # Intersection
A - B    # Difference
A ^ B    # Symmetric difference
```

---

# Set Methods Quick Reference

| Method                   | Purpose                                         |
| ------------------------ | ----------------------------------------------- |
| `add()`                  | Adds one element                                |
| `remove()`               | Removes an element; raises `KeyError` if absent |
| `discard()`              | Removes an element if present                   |
| `pop()`                  | Removes and returns an arbitrary element        |
| `clear()`                | Removes all elements                            |
| `union()`                | Combines unique elements                        |
| `intersection()`         | Finds common elements                           |
| `difference()`           | Finds elements present only in the first set    |
| `symmetric_difference()` | Finds non-common elements                       |
| `isdisjoint()`           | Checks whether sets have no common elements     |
| `issubset()`             | Checks whether one set is contained in another  |
| `issuperset()`           | Checks whether one set contains another         |

---

# Set vs List vs Tuple

| Feature       | List               | Tuple            | Set                                |
| ------------- | ------------------ | ---------------- | ---------------------------------- |
| Ordered       | Yes                | Yes              | No guaranteed positional order     |
| Mutable       | Yes                | No               | Yes                                |
| Indexed       | Yes                | Yes              | No                                 |
| Slicing       | Yes                | Yes              | No                                 |
| Duplicates    | Allowed            | Allowed          | Not allowed                        |
| Heterogeneous | Yes                | Yes              | Yes, if elements are hashable      |
| Main use      | General collection | Fixed collection | Unique collection / set operations |
| Syntax        | `[ ]`              | `( )`            | `{ }`                              |

### Easy way to remember

```text
List  → Ordered + Mutable + Duplicates
Tuple → Ordered + Immutable + Duplicates
Set   → Unique + Mutable + No Indexing
```

---

# Important Points to Remember

* Sets store **unique elements**.
* Sets do not support indexing or slicing.
* Sets are mutable.
* Set elements must be **hashable**.
* Lists and dictionaries cannot normally be direct elements of a set because they are mutable and unhashable.
* Tuples can be set elements when their contents are hashable.
* An empty set is created using `set()`, not `{}`.
* `{}` creates an empty dictionary.
* `add()` adds one element.
* `remove()` raises `KeyError` if the element is absent.
* `discard()` does not raise an error if the element is absent.
* `pop()` removes an arbitrary element; do not assume which element it will remove.
* `clear()` empties the set.
* `union()` combines sets.
* `intersection()` finds common elements.
* `difference()` finds elements present in one set but not the other.
* `symmetric_difference()` finds elements that are not common.
* `issubset()` checks containment.
* `issuperset()` checks reverse containment.
* `isdisjoint()` checks whether two sets have no common elements.
* `sorted()` returns a list, not a set.

### One-line memory trick

```text
Create    → set()
Unique    → No duplicates
Add       → add()
Delete    → remove / discard / pop
Clear     → clear()
Search    → in / not in
Combine   → union
Common    → intersection
Only A    → difference
Not common → symmetric_difference
Contained → issubset
Contains  → issuperset
No common → isdisjoint
```
