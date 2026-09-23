# Python Dictionaries

A **dictionary** is a built-in Python data type used to store data in **key-value pairs**.

Each item in a dictionary has the form:

```python
key : value
```

Example:

```python
d = {"name": "kushagra", "age": 21}
```

Here:

```text
"name" → key
"kushagra" → value

"age" → key
21 → value
```

Dictionaries are useful when data needs to be accessed using a **meaningful key** instead of a numerical index.

---

# 1. Rules of Dictionaries

## Rule 1: Dictionaries Do Not Use Indexing

Dictionaries do not use numerical indexes like lists and tuples.

Instead, values are accessed using their **keys**.

```python
d = {1:"Apple", 2:"Ball", 3:"Cat"}

print(d[2])
```

Here `2` is a key, not an index.

Output:

```text
Ball
```

---

## Rule 2: Dictionaries Are Mutable

A dictionary can be modified after it is created.

You can:

* Add new key-value pairs.
* Change existing values.
* Delete key-value pairs.
* Clear the dictionary.

Example:

```python
d = {1:"Apple", 2:"Ball"}

d[1] = "Ant"

print(d)
```

The dictionary has been modified.

---

## Rule 3: Keys Must Be Immutable / Hashable

Dictionary keys must be **hashable**.

Common examples of valid keys:

```text
int
float
string
tuple (if its elements are hashable)
```

A list cannot be used as a key because lists are mutable.

```python
# d = {[1, 2]:"kushagra", "age":21}
```

This raises a `TypeError`.

A tuple can be used as a key:

```python
d = {(1, 2):"kushagra", "age":21}

print(d)
```

This works because the tuple is hashable when its elements are hashable.

### Values are different

Values do not have this restriction.

Values can be mutable objects such as lists or dictionaries.

---

## Rule 4: Keys Should Be Unique

A dictionary cannot contain multiple separate entries with the same key.

Consider:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat"}

print(d)
```

Now:

```python
d = {1:"Apple", 2:"Ball", 1:"Cat"}

print(d)
```

Output:

```text
{1: 'Cat', 2: 'Ball'}
```

The second occurrence of key `1` replaces the previous value.

So:

```text
Same key → value gets updated
```

---

# 2. Creating a Dictionary

An empty dictionary can be created using `{}`:

```python
d = {}

print(d)
```

Output:

```text
{}
```

A dictionary can also be created with key-value pairs:

```python
d = {"name":"kushagra", "age":21}

print(d)
```

Output:

```text
{'name': 'kushagra', 'age': 21}
```

---

# 3. Nested / 2D Dictionary

A dictionary can contain another dictionary as a value.

```python
d = {
    "Name":"Kushagra",
    "Language":"Python",
    "Marks":{
        "A":45,
        "B":48,
        "C":50
    }
}

print(d)
```

Here `"Marks"` contains another dictionary.

Structure:

```text
d
│
├── Name     → Kushagra
├── Language → Python
└── Marks
    ├── A → 45
    ├── B → 48
    └── C → 50
```

This is called a **nested dictionary**.

---

# 4. Accessing Dictionary Data

Consider:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

print(d)
```

Unlike a list:

```python
# d[0]
```

is not used to access the first item.

Instead, provide the required **key**:

```python
print(d[2])
```

Output:

```text
Ball
```

The general syntax is:

```python
dictionary[key]
```

---

# 5. Using `get()`

The `get()` method can also be used to retrieve a value.

```python
print(d.get(5))
```

Output:

```text
Elephant
```

### `[]` vs `get()`

If the key exists:

```python
d[5]
```

and:

```python
d.get(5)
```

both return the value.

However, if the key does not exist:

```python
d[10]
```

raises a `KeyError`.

Whereas:

```python
d.get(10)
```

returns:

```text
None
```

This makes `get()` useful when a key may not exist.

---

# 6. Accessing Nested Dictionaries

Consider:

```python
d = {
    "Name":"Kushagra",
    "Language":"Python",
    "Marks":{
        "A":45,
        "B":48,
        "C":50
    }
}
```

Access the `"Marks"` dictionary:

```python
print(d["Marks"])
```

Output:

```text
{'A': 45, 'B': 48, 'C': 50}
```

Access the value of `"A"`:

```python
print(d["Marks"]["A"])
```

Output:

```text
45
```

Here:

```text
d["Marks"]       → inner dictionary
d["Marks"]["A"]  → value 45
```

---

# 7. Editing a Dictionary

Dictionaries are mutable, so existing values can be changed.

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

print(d)

d[3] = "Crow"

print(d)
```

Output:

```text
{1: 'Apple', 2: 'Ball', 3: 'Cat', 4: 'Dog', 5: 'Elephant'}
{1: 'Apple', 2: 'Ball', 3: 'Crow', 4: 'Dog', 5: 'Elephant'}
```

The key `3` already existed, so its value was updated.

---

# 8. Adding a New Key-Value Pair

If the specified key does not exist, assigning a value creates a new key-value pair.

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

d[6] = "Fast"

print(d)
```

Output:

```text
{1: 'Apple', 2: 'Ball', 3: 'Cat', 4: 'Dog', 5: 'Elephant', 6: 'Fast'}
```

So the same syntax can perform two different operations:

```text
Existing key → Update value
New key      → Add key-value pair
```

---

# 9. Deleting Dictionary Data

## `del`

`del` can delete the entire dictionary:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

del d
```

After this, the variable `d` no longer exists.

It can also delete a specific key-value pair:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

del d[3]

print(d)
```

Output:

```text
{1: 'Apple', 2: 'Ball', 4: 'Dog', 5: 'Elephant'}
```

---

## `clear()`

`clear()` removes all key-value pairs but keeps the dictionary itself.

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

d.clear()

print(d)
```

Output:

```text
{}
```

### Difference

```text
del d     → deletes the dictionary variable
d.clear() → empties the dictionary
```

---

# 10. Iterating Through a Dictionary

A `for` loop can be used to iterate through a dictionary.

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

for i in d:
    print(i, d[i])
```

Output:

```text
1 Apple
2 Ball
3 Cat
4 Dog
5 Elephant
```

When you directly iterate over a dictionary:

```python
for i in d:
```

`i` represents the **keys**.

Then:

```python
d[i]
```

is used to access the corresponding value.

---

# 11. Membership Operations

Membership checking in a dictionary is performed on **keys by default**.

```python
print(1 in d)
```

This checks whether `1` exists as a key.

For:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat"}
```

```python
1 in d
```

returns:

```text
True
```

But:

```python
"Apple" in d
```

returns:

```text
False
```

because `"Apple"` is a value, not a key.

### Checking values

To check values specifically, use:

```python
"Apple" in d.values()
```

---

# 12. Dictionary Functions

Consider:

```python
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
```

---

## `len()`

Returns the number of key-value pairs.

```python
print(len(d))
```

Output:

```text
5
```

---

## `min()`

Returns the smallest key.

```python
print(min(d))
```

Output:

```text
1
```

---

## `max()`

Returns the largest key.

```python
print(max(d))
```

Output:

```text
5
```

---

## `sum()`

`sum()` works on the dictionary's keys when they are numeric.

```python
print(sum(d))
```

Output:

```text
15
```

It effectively sums:

```text
1 + 2 + 3 + 4 + 5
```

---

## `sorted()`

`sorted()` sorts the dictionary's keys and returns them as a **list**.

```python
print(sorted(d))
```

Output:

```text
[1, 2, 3, 4, 5]
```

Reverse order:

```python
print(sorted(d, reverse=True))
```

Output:

```text
[5, 4, 3, 2, 1]
```

### Important

`sorted(d)` does not sort the dictionary itself. It returns a list containing the sorted keys.

---

# 13. `keys()`

The `keys()` method returns a view containing all dictionary keys.

```python
print(d.keys())
```

Example output:

```text
dict_keys([1, 2, 3, 4, 5])
```

You can convert it into a list if required:

```python
print(list(d.keys()))
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

# 14. `values()`

The `values()` method returns a view containing all dictionary values.

```python
print(d.values())
```

Example output:

```text
dict_values(['Apple', 'Ball', 'Cat', 'Dog', 'Elephant'])
```

You can also convert it into a list:

```python
print(list(d.values()))
```

Output:

```text
['Apple', 'Ball', 'Cat', 'Dog', 'Elephant']
```

---

# 15. `items()`

Another important dictionary method is `items()`.

It returns the key-value pairs together.

```python
print(d.items())
```

Example output:

```text
dict_items([
    (1, 'Apple'),
    (2, 'Ball'),
    (3, 'Cat'),
    (4, 'Dog'),
    (5, 'Elephant')
])
```

This is especially useful when looping through both keys and values:

```python
for key, value in d.items():
    print(key, value)
```

Output:

```text
1 Apple
2 Ball
3 Cat
4 Dog
5 Elephant
```

---

# Dictionary Methods Quick Reference

| Method      | Purpose                                              |
| ----------- | ---------------------------------------------------- |
| `get()`     | Safely retrieves a value                             |
| `keys()`    | Returns dictionary keys                              |
| `values()`  | Returns dictionary values                            |
| `items()`   | Returns key-value pairs                              |
| `clear()`   | Removes all pairs                                    |
| `pop()`     | Removes and returns a specified key's value          |
| `popitem()` | Removes and returns the last inserted key-value pair |
| `update()`  | Adds or updates key-value pairs                      |

---

# Dictionary vs List vs Tuple vs Set

| Feature        | List    | Tuple   | Set                 | Dictionary           |
| -------------- | ------- | ------- | ------------------- | -------------------- |
| Ordered        | Yes     | Yes     | No positional order | Yes, insertion order |
| Mutable        | Yes     | No      | Yes                 | Yes                  |
| Indexed        | Yes     | Yes     | No                  | No                   |
| Duplicates     | Allowed | Allowed | Not allowed         | Keys: no duplicates  |
| Access         | Index   | Index   | Membership          | Key                  |
| Main structure | Values  | Values  | Unique values       | Key-value pairs      |
| Syntax         | `[ ]`   | `( )`   | `{ }`               | `{key: value}`       |

### Easy way to remember

```text
List       → [values]
Tuple      → (values)
Set        → {unique values}
Dictionary → {key: value}
```

---

# Important Points to Remember

* A dictionary stores data as **key-value pairs**.
* Dictionaries are mutable.
* Dictionaries do not use numerical indexing.
* Values are accessed using their **keys**.
* Dictionary keys must be **hashable**.
* Dictionary values can be mutable.
* Keys must be unique.
* If the same key is written again, its value is updated.
* `d[key]` accesses a value directly.
* `d.get(key)` safely retrieves a value and returns `None` if the key does not exist.
* Assigning to an existing key updates its value.
* Assigning to a new key creates a new key-value pair.
* `del` can delete a key-value pair or the entire dictionary.
* `clear()` empties the dictionary.
* `in` checks **keys by default**.
* `keys()` gives the keys.
* `values()` gives the values.
* `items()` gives key-value pairs.
* `sorted(d)` sorts the dictionary's keys and returns a list.
* `len(d)` counts the number of key-value pairs.

### One-line memory trick

```text
Create   → {}
Access   → d[key] / d.get(key)
Add      → d[new_key] = value
Update   → d[existing_key] = new_value
Delete   → del / pop()
Clear    → clear()
Keys     → keys()
Values   → values()
Pairs    → items()
Search   → key in d
Loop     → for key, value in d.items()
```
