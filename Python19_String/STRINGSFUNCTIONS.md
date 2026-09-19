# Python String Functions

String functions and methods are used to **analyze, modify, search, split, format, and transform strings**.

Python provides many built-in functions and string methods that make string manipulation easier.

---

## 1. `len()`

`len()` returns the **number of characters** in a string.

```python
k = "Kushagra"

print(len(k))
```

### Output

```text
8
```

`len()` also counts spaces and special characters.

---

## 2. `max()`

`max()` returns the character with the **highest Unicode value** from the string.

```python
print(max(k))
```

For `"Kushagra"`, the result is:

```text
u
```

The comparison is based on Unicode/code-point values, not alphabetical position alone.

---

## 3. `min()`

`min()` returns the character with the **lowest Unicode value**.

```python
print(min(k))
```

For `"Kushagra"`, the result is:

```text
K
```

---

## 4. `sorted()`

`sorted()` returns the characters of a string in sorted order as a **list**.

```python
print(sorted(k))
```

### Reverse sorting

```python
print(sorted(k, reverse=True))
```

`reverse=True` sorts the characters in descending order.

### Important

`sorted()` does **not** return a string.

```python
sorted("Kushagra")
```

returns something like:

```text
['K', 'a', 'a', 'g', 'h', 'k', 'r', 'u']
```

---

# String Case Functions

These methods are used to change the capitalization of strings.

---

## 5. `capitalize()`

`capitalize()` converts the **first character to uppercase** and the remaining characters to lowercase.

```python
k = "kushagra"

print(k.capitalize())
```

### Output

```text
Kushagra
```

---

## 6. `title()`

`title()` converts the first character of **each word** to uppercase.

```python
k = "working on python"

print(k.title())
```

### Output

```text
Working On Python
```

---

## 7. `upper()`

`upper()` converts all alphabetic characters to uppercase.

```python
k = "kushagra"

print(k.upper())
```

### Output

```text
KUSHAGRA
```

---

## 8. `lower()`

`lower()` converts all alphabetic characters to lowercase.

```python
k = "KUSHAGRA"

print(k.lower())
```

### Output

```text
kushagra
```

---

## 9. `swapcase()`

`swapcase()` changes uppercase characters to lowercase and lowercase characters to uppercase.

```python
k = "KuSHagrA"

print(k.swapcase())
```

### Output

```text
kUsHaGRA
```

---

# Searching and Counting

## 10. `count()`

`count()` returns the number of times a substring occurs in a string.

```python
k = "elephant elephant"

print(k.count('e'))

print(k.count('ele'))
```

### Output

```text
4
2
```

The search is **case-sensitive**.

---

## 11. `find()`

`find()` returns the index of the **first occurrence** of a substring.

```python
k = "kushagra"

print(k.find("a"))

print(k.find("m"))
```

Output:

```text
5
-1
```

If the substring is not found, `find()` returns:

```text
-1
```

---

## 12. `index()`

`index()` also returns the index of the first occurrence.

```python
k = "kushagra"

print(k.index("a"))
```

Output:

```text
5
```

### Difference between `find()` and `index()`

```python
k.find("m")
```

returns:

```text
-1
```

while:

```python
k.index("m")
```

raises a `ValueError`.

```python
# print(k.index("a")) -> works
# print(k.index("m")) -> error
```

### Quick difference

| Method    | If substring is not found |
| --------- | ------------------------- |
| `find()`  | Returns `-1`              |
| `index()` | Raises `ValueError`       |

---

# Checking the Beginning and End

## 13. `startswith()`

`startswith()` checks whether a string begins with a particular substring.

It returns either `True` or `False`.

```python
k = "It is a good day"

print(k.startswith("It"))
```

Output:

```text
True
```

---

## 14. `endswith()`

`endswith()` checks whether a string ends with a particular substring.

```python
k = "It is a good day"

print(k.endswith("ay"))
```

Output:

```text
True
```

These methods are useful when validating filenames, URLs, extensions, prefixes, etc.

---

# String Formatting

## 15. `format()`

`format()` inserts values into placeholders `{}` inside a string.

### Positional formatting

```python
k = "Hello my name is {} and I am {}"

print(k.format("Kushagra", 21))
```

Output:

```text
Hello my name is Kushagra and I am 21
```

The values are inserted according to their position.

---

### Indexed formatting

```python
k = "Hello my name is {1} and I am {0}"

print(k.format("Kushagra", 21))
```

Here:

```text
{0} → Kushagra
{1} → 21
```

Therefore:

```text
Hello my name is 21 and I am Kushagra
```

---

### Named formatting

```python
k = "Hello my name is {name} and I am {age}"

print(k.format(name="Kushagra", age=21))
```

Output:

```text
Hello my name is Kushagra and I am 21
```

Named placeholders are often easier to understand when there are many values.

> Modern Python code also commonly uses **f-strings** for formatting, but `format()` is important to understand because it is a fundamental string-formatting method.

---

# Checking String Content

These methods return `True` or `False` depending on the characters present in the string.

---

## 16. `isalnum()`

`isalnum()` returns `True` if all characters are **alphabetic or numeric** and the string is not empty.

```python
k = "Weight999"

print(k.isalnum())
```

Output:

```text
True
```

Spaces and special characters make it return `False`.

---

## 17. `isalpha()`

`isalpha()` returns `True` if all characters are alphabetic.

```python
k = "Weight"

print(k.isalpha())
```

Output:

```text
True
```

For example:

```python
"Weight999".isalpha()
```

would return:

```text
False
```

---

## 18. `isdecimal()`

`isdecimal()` returns `True` when all characters are decimal characters.

Example:

```python
print("20".isdecimal())
```

Output:

```text
True
```

It is more restrictive than `isdigit()`.

---

## 19. `isdigit()`

`isdigit()` checks whether all characters are digits.

```python
k = "20"

print(k.isdigit())
```

Output:

```text
True
```

It is useful when checking whether a string contains digit characters before converting it to a number.

---

## 20. `isidentifier()`

`isidentifier()` checks whether a string follows Python's rules for a valid **identifier**.

```python
k = "hello_kushagra"

print(k.isidentifier())
```

Output:

```text
True
```

For example:

```python
"hello-world".isidentifier()
```

returns:

```text
False
```

because `-` is not allowed inside a Python identifier.

### Important

A string can satisfy `isidentifier()` but still be a Python keyword.

For example:

```python
"for".isidentifier()
```

returns:

```text
True
```

but `for` cannot be used as a variable name because it is a keyword.

---

# Splitting and Joining

## 21. `split()`

`split()` breaks a string into smaller parts and returns them as a **list**.

```python
k = "I am working on python"

print(k.split())
```

Output:

```text
['I', 'am', 'working', 'on', 'python']
```

When no separator is provided, whitespace is used as the separator.

---

### Splitting using a specific separator

```python
print(k.split("on"))
```

Output:

```text
['I am working ', ' python']
```

The specified separator is removed from the resulting parts.

---

## 22. `join()`

`join()` combines elements of an iterable into a single string using the string on which the method is called as the separator.

```python
k = "-"

print(k.join(['I', 'am', 'working', 'on', 'python']))
```

Output:

```text
I-am-working-on-python
```

### Easy way to remember

```text
split() → String → List
join()  → List → String
```

---

# Replacing Content

## 23. `replace()`

`replace()` replaces one substring with another.

```python
k = "I am kushagra"

print(k.replace("kushagra", "lion"))
```

Output:

```text
I am lion
```

The original string is not changed because strings are **immutable**.

Instead, `replace()` creates and returns a new string.

---

# Removing Extra Characters

## 24. `strip()`

`strip()` removes leading and trailing whitespace from a string.

```python
k = "           kushagra       "

print(k.strip())
```

Output:

```text
kushagra
```

It removes whitespace from the **beginning and end**, but not from the middle.

For example:

```python
"   hello world   ".strip()
```

becomes:

```text
"hello world"
```

### Related methods

```python
k.lstrip()
```

Removes whitespace from the left side.

```python
k.rstrip()
```

Removes whitespace from the right side.

---

# Quick Reference

| Function / Method | Purpose                                      |
| ----------------- | -------------------------------------------- |
| `len()`           | Returns number of characters                 |
| `max()`           | Returns character with highest Unicode value |
| `min()`           | Returns character with lowest Unicode value  |
| `sorted()`        | Returns sorted characters as a list          |
| `capitalize()`    | Capitalizes first character                  |
| `title()`         | Capitalizes first character of each word     |
| `upper()`         | Converts to uppercase                        |
| `lower()`         | Converts to lowercase                        |
| `swapcase()`      | Swaps uppercase and lowercase                |
| `count()`         | Counts occurrences                           |
| `find()`          | Finds position, returns `-1` if absent       |
| `index()`         | Finds position, raises error if absent       |
| `startswith()`    | Checks beginning of string                   |
| `endswith()`      | Checks end of string                         |
| `format()`        | Inserts values into placeholders             |
| `isalnum()`       | Checks alphabetic/numeric characters         |
| `isalpha()`       | Checks alphabetic characters                 |
| `isdecimal()`     | Checks decimal characters                    |
| `isdigit()`       | Checks digit characters                      |
| `isidentifier()`  | Checks valid Python identifier syntax        |
| `split()`         | Splits string into a list                    |
| `join()`          | Combines elements into a string              |
| `replace()`       | Replaces substring                           |
| `strip()`         | Removes leading/trailing whitespace          |

---

# Important Points

* Most string methods **do not modify the original string** because strings are immutable.
* Instead, they return a **new string** or another result.
* `find()` returns `-1` when something is not found, while `index()` raises `ValueError`.
* `split()` converts a string into a list, while `join()` combines multiple strings into one.
* `startswith()` and `endswith()` are useful for checking prefixes and suffixes.
* `isalpha()`, `isdigit()`, `isalnum()`, etc. are useful for validating user input.
* String comparisons and many character-based operations are **case-sensitive**.
* `sorted()` returns a list even when the input is a string.
* `strip()` removes characters only from the beginning and end, not from the middle.

### One-line memory trick

```text
Analyze → len, max, min, count
Change case → capitalize, title, upper, lower, swapcase
Search → find, index
Check → startswith, endswith, isalpha, isdigit, isalnum
Format → format
Split/Combine → split, join
Modify content → replace
Clean → strip
```
