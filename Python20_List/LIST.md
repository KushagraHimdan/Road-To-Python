# Python Lists

A **list** is a built-in Python data type used to store multiple values in a single variable.

Lists are:

* **Ordered** — items maintain their position.
* **Mutable** — items can be changed after the list is created.
* **Heterogeneous** — different data types can be stored together.
* **Dynamic** — items can be added or removed after creation.
* **Indexed** — each item has a position starting from `0`.
* **Allow duplicates** — the same value can occur multiple times.

---

# 1. List vs Array

A traditional array generally stores elements of the **same data type**, while a Python list can store elements of different data types.

| Feature                 | Array                                  | Python List                   |
| ----------------------- | -------------------------------------- | ----------------------------- |
| Data types              | Usually homogeneous                    | Can be heterogeneous          |
| Memory                  | Typically contiguous element storage   | Stores references to objects  |
| Flexibility             | More restricted                        | More flexible                 |
| Operations              | Generally optimized for numerical data | Rich built-in operations      |
| Programmer friendliness | More specialized                       | Very convenient and versatile |

### Example of a homogeneous list

```python
l = [1, 2, 3, 4, 5]
```

### Example of a heterogeneous list

```python
l = [1, 3.4, "kushagra", True, 5+6j]
```

### Important

It is common to say that arrays are **faster than lists**, but this is context-dependent. Python lists are highly optimized general-purpose containers, while specialized arrays can be more memory-efficient and faster for particular numerical workloads.

---

# 2. Creating a List

An empty list can be created using square brackets:

```python
l = []
```

You can also create a list from another iterable using `list()`.

```python
l = list("Kushgara")

print(l)
```

Output:

```text
['K', 'u', 's', 'h', 'g', 'a', 'r', 'a']
```

The characters of the string become individual elements of the list.

---

# 3. Homogeneous List

A list containing values of the same data type is called a **homogeneous list**.

```python
l = [1, 2, 3, 4, 5]

print(l)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

# 4. Heterogeneous List

A list can contain values of different data types.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

print(l)
```

Here the list contains:

* `int`
* `float`
* `str`
* `bool`
* `complex`

This flexibility is one of the major characteristics of Python lists.

---

# 5. Multidimensional Lists

A list can contain other lists. This allows us to create structures resembling multidimensional arrays.

## 2D List

```python
l = [12, 14, [23, 45]]

print(l)
```

The third element itself is another list.

A more conventional 2D structure would be:

```python
l = [[1, 2], [3, 4]]
```

---

## 3D List

A list can contain lists that contain other lists.

```python
l = [[[1,2], [3, 4]],[[5, 6], [6, 7]]]

print(l)
```

The structure can be visualized as:

```text
[
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [6, 7]
    ]
]
```

The deeper the nesting, the more indexes are required to access an individual element.

---

# 6. Accessing Data from a List

Lists use **zero-based indexing**.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

print(l[2])
```

Output:

```text
kushagra
```

Index positions:

```text
1        → index 0
3.4      → index 1
kushagra → index 2
True     → index 3
5+6j     → index 4
```

---

## Slicing

Lists support slicing just like strings.

```python
print(l[2:4])
```

Output:

```text
['kushagra', True]
```

The ending index is **excluded**.

### Reverse a list

```python
print(l[::-1])
```

This returns the list in reverse order.

---

# 7. Accessing Nested Lists

Consider:

```python
l = [12, 14, [23, 45]]
```

The nested list can be accessed using another index.

```python
print(l[-1])
```

Output:

```text
[23, 45]
```

Access the second element inside the nested list:

```python
print(l[2][1])
```

Output:

```text
45
```

The same element can also be accessed using negative indexing:

```python
print(l[-1][1])
```

Output:

```text
45
```

---

## Accessing a 3D List

```python
l = [[[1,2], [3, 4, 7]],[[5, 6], [6, 7]]]

print(l[0][1][2])
```

Output:

```text
7
```

Think of it as:

```text
l[0]       → first outer list
l[0][1]    → second inner list
l[0][1][2] → third element
```

---

# 8. Editing a List

Lists are **mutable**, which means their elements can be changed after creation.

```python
l = [1, 2, 3, 4, 5]

l[2] = 12

print(l)
```

Output:

```text
[1, 2, 12, 4, 5]
```

---

## Editing Multiple Elements

Slicing can also be used to replace multiple elements.

```python
l[1:4] = [200, 300, 400]

print(l)
```

Output:

```text
[1, 200, 300, 400, 5]
```

Unlike strings, lists allow direct modification of their elements.

---

# 9. Adding Items to a List

Python provides several methods for adding elements.

---

## `append()`

`append()` adds **one item** to the end of the list.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

l.append(190)

print(l)
```

Output:

```text
[1, 3.4, 'kushagra', True, (5+6j), 190]
```

Even if you append a list, the entire list becomes **one element**.

```python
l.append([190, "Tiger"])
```

The result contains:

```text
[190, "Tiger"]
```

as a single nested element.

---

## `extend()`

`extend()` adds **multiple elements** from another iterable.

```python
l.extend(["Lion", 499])

print(l)
```

Both `"Lion"` and `499` are added as separate elements.

### `append()` vs `extend()`

```python
l = [1, 2]

l.append([3, 4])
```

Result:

```text
[1, 2, [3, 4]]
```

Whereas:

```python
l = [1, 2]

l.extend([3, 4])
```

Result:

```text
[1, 2, 3, 4]
```

### Important

`extend()` works with any iterable.

Your example:

```python
l.extend("Laptop")

print(l)
```

adds each character separately:

```text
'L', 'a', 'p', 't', 'o', 'p'
```

---

## `insert()`

`insert()` adds an element at a specific position.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

l.insert(4, "Lion")

print(l)
```

The general syntax is:

```python
list.insert(index, value)
```

The existing elements are shifted to make room for the new item.

---

# 10. Deleting Items

Python provides several ways to remove items from a list.

---

## `del`

`del` can delete an entire list:

```python
l = [1, 3.4, "kushagra", True, 5+6j]

del l
```

After this, the variable `l` no longer exists.

It can also delete an individual element:

```python
l = [1, 3.4, "kushagra", True, 5+6j]

del l[-1]

print(l)
```

Output:

```text
[1, 3.4, 'kushagra', True]
```

`del` can also remove slices.

---

## `remove()`

`remove()` deletes the **first occurrence of a specified value**.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

l.remove(3.4)

print(l)
```

Output:

```text
[1, 'kushagra', True, (5+6j)]
```

If the value does not exist, `remove()` raises a `ValueError`.

---

## `pop()`

`pop()` removes and **returns an element**.

Without an index, it removes the last element.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

l.pop()

print(l)
```

The last element is removed.

You can also specify an index:

```python
l.pop(1)
```

This removes the element at index `1`.

---

## `clear()`

`clear()` removes all elements from the list but keeps the list itself.

```python
l = [1, 3.4, "kushagra", True, 5+6j]

l.clear()

print(l)
```

Output:

```text
[]
```

### Difference

```text
del l      → deletes the list variable
l.clear()  → empties the list
```

---

# 11. List Operations

## Addition / Concatenation

The `+` operator combines two lists.

```python
l = [1, 2, 3, 4, 5]

m = [10, 11, 12, 13]

k = l + m

print(k)
```

Output:

```text
[1, 2, 3, 4, 5, 10, 11, 12, 13]
```

The original lists remain unchanged.

---

## Multiplication

The `*` operator repeats a list.

```python
k = l * 3

print(k)
```

Output:

```text
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```

---

# 12. Iterating Through a List

A `for` loop can be used to access each element.

```python
for i in l:
    print(i)
```

For:

```python
l = [1, 2, 3, 4, 5]
```

the loop processes:

```text
1
2
3
4
5
```

one element at a time.

---

# 13. Membership Operations

The `in` operator checks whether an element exists in a list.

```python
print(3 in l)
```

Output:

```text
True
```

Similarly:

```python
print(10 in l)
```

would return:

```text
False
```

The `not in` operator checks that an element does not exist.

```python
print(10 not in l)
```

---

# 14. Built-in Functions for Lists

Python provides several built-in functions that work with lists.

```python
l = [1, 2, 3, 4, 5]

m = len(l)

print(m)

print(min(l))

print(max(l))
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

---

# 15. `sorted()`

`sorted()` returns a **new sorted list**.

```python
l = [1, 9, 3, 7, 5]

print(sorted(l))

print(sorted(l, reverse=True))

print(l)
```

Output:

```text
[1, 3, 5, 7, 9]
[9, 7, 5, 3, 1]
[1, 9, 3, 7, 5]
```

Notice that the original list remains unchanged.

```python
sorted(l)
```

creates and returns a new sorted list.

---

# 16. `sort()`

`sort()` sorts the **original list in place**.

```python
l = [1, 9, 3, 7, 5]

l.sort()

print(l)
```

Output:

```text
[1, 3, 5, 7, 9]
```

For descending order:

```python
l.sort(reverse=True)

print(l)
```

Output:

```text
[9, 7, 5, 3, 1]
```

### `sorted()` vs `sort()`

| `sorted()`                      | `sort()`                        |
| ------------------------------- | ------------------------------- |
| Built-in function               | List method                     |
| Returns a new list              | Modifies the original list      |
| Original list remains unchanged | Original list is changed        |
| Works with many iterables       | Available specifically on lists |

### Easy memory trick

```text
sorted() → creates a sorted copy
sort()   → sorts the original list
```

---

# 17. `index()`

`index()` returns the index of the **first occurrence** of a specified value.

```python
l = [1, 9, 3, 7, 5]

print(l.index(9))
```

Output:

```text
1
```

If the value is not present, `index()` raises a `ValueError`.

---

# List Methods Quick Reference

| Method     | Purpose                          |
| ---------- | -------------------------------- |
| `append()` | Adds one item at the end         |
| `extend()` | Adds multiple items              |
| `insert()` | Adds an item at a specific index |
| `remove()` | Removes the first matching value |
| `pop()`    | Removes and returns an item      |
| `clear()`  | Removes all items                |
| `sort()`   | Sorts the list in place          |
| `index()`  | Finds the index of a value       |

---

# List Functions Quick Reference

| Function   | Purpose                         |
| ---------- | ------------------------------- |
| `len()`    | Returns number of elements      |
| `min()`    | Returns smallest element        |
| `max()`    | Returns largest element         |
| `sorted()` | Returns a new sorted list       |
| `list()`   | Creates a list from an iterable |

---

# Important Points to Remember

* Lists are **ordered and mutable**.
* Lists can contain different data types.
* List indexing starts from `0`.
* Negative indexing starts from `-1`.
* Lists support slicing.
* A list can contain another list, creating nested or multidimensional structures.
* `append()` adds one item.
* `extend()` adds elements from an iterable.
* `insert()` adds an item at a specific position.
* `remove()` removes a value.
* `pop()` removes an item using its index and returns it.
* `clear()` empties the list.
* `del` can delete an item, a slice, or the entire list variable.
* `sorted()` returns a new sorted list.
* `sort()` changes the original list.
* `index()` returns the position of the first matching value.
* Lists can be combined using `+` and repeated using `*`.
* `in` and `not in` can be used to check membership.

### One-line memory trick

```text
Create → []
Access → index / slice
Add → append / extend / insert
Delete → del / remove / pop / clear
Search → index / in
Sort → sorted / sort
Repeat → *
Combine → +
Iterate → for
```
