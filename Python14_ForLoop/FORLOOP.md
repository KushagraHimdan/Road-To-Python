# Python For Loop

## What is a For Loop?

A **for loop** is an iteration control statement used to repeat a block of code by iterating over a **range** or the elements of a **sequence/iterable**.

### Basic Syntax

```python
for variable in iterable:
    # code to execute
```

The `for` loop takes one value at a time from the iterable and executes the loop body.

---

# `range()` Function

The `range()` function generates a sequence of integers within a specified range.

### Basic Syntax

```python
range(start, stop, step)
```

| Parameter | Meaning                               |
| --------- | ------------------------------------- |
| `start`   | Starting value                        |
| `stop`    | Ending limit, **not included**        |
| `step`    | Difference between consecutive values |

---

## 1. Start and Stop

```python
ls1 = list(range(1, 11))

print(ls1)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Here:

```python
range(1, 11)
```

starts from `1` and stops **before `11`**.

Therefore, `11` is not included.

### Important Rule

> **The stop value in `range()` is always excluded.**

---

## 2. Providing Only One Number

If only one number is provided:

```python
range(5)
```

Python treats it as:

```python
range(0, 5)
```

Example:

```python
ls2 = list(range(11))

print(ls2)
```

Output:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

So:

```python
range(11)
```

means:

```python
range(0, 11)
```

The default starting value is `0`.

---

## 3. Using the Step Parameter

By default, the step is `1`.

We can change it by providing a third argument.

```python
ls3 = list(range(1, 11, 2))

print(ls3)
```

Output:

```text
[1, 3, 5, 7, 9]
```

Here:

```python
range(1, 11, 2)
```

means:

* Start at `1`
* Stop before `11`
* Increase by `2`

---

## 4. Backward Printing

A negative step can be used to move backwards.

```python
ls4 = list(range(10, 0, -1))

print(ls4)
```

Output:

```text
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

Here:

```python
range(10, 0, -1)
```

means:

* Start at `10`
* Stop before `0`
* Decrease by `1`

---

# `range()` Summary

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
range(5)
# 0, 1, 2, 3, 4

range(1, 5)
# 1, 2, 3, 4

range(1, 10, 2)
# 1, 3, 5, 7, 9

range(10, 0, -2)
# 10, 8, 6, 4, 2
```

---

# Sequences and Iterables

An **iterable** is an object whose elements can be accessed one at a time during iteration.

Common examples include:

* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* `range` objects

### Important distinction

Strings, lists, and tuples preserve a defined order.

Sets are **unordered collections**, so their iteration order should not be relied upon.

---

# For Loop with `range()`

A `for` loop can directly iterate over a `range()` object.

```python
for i in range(1, 11):

    print(i)
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

---

## For Loop with Step

```python
for i in range(1, 11, 2):

    print(i)
```

Output:

```text
1
3
5
7
9
```

The loop moves forward by `2` each time.

---

## For Loop in Reverse

```python
for i in range(10, 0, -2):

    print(i)
```

Output:

```text
10
8
6
4
2
```

The loop moves backwards by `2`.

---

# For Loop with a String

A `for` loop can iterate over the characters of a string.

```python
for i in "Kushagra":

    print(i)
```

Output:

```text
K
u
s
h
a
g
r
a
```

Here, `i` receives one character at a time.

The loop effectively works like:

```text
i = K
i = u
i = s
i = h
i = a
i = g
i = r
i = a
```

---

# `range()` vs `list(range())`

There is an important difference between:

```python
range(1, 11)
```

and:

```python
list(range(1, 11))
```

`range()` creates a **range object** that represents the sequence.

```python
print(range(1, 11))
```

Output:

```text
range(1, 11)
```

`list()` converts that range into an actual list:

```python
print(list(range(1, 11)))
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

You usually do **not** need to convert `range()` to a list just to use it in a `for` loop.

```python
for i in range(1, 11):
    print(i)
```

---

# While Loop vs For Loop

| While Loop                                                  | For Loop                                                |
| ----------------------------------------------------------- | ------------------------------------------------------- |
| Repeats while a condition is `True`                         | Iterates over an iterable                               |
| Usually requires initialization and updating                | Iteration is handled automatically                      |
| Useful when the number of iterations depends on a condition | Useful when iterating over ranges, strings, lists, etc. |
| Can accidentally create an infinite loop                    | Generally easier to control                             |

Example:

```python
# While loop
i = 1

while i <= 5:
    print(i)
    i += 1
```

```python
# For loop
for i in range(1, 6):
    print(i)
```

Both produce:

```text
1
2
3
4
5
```

---

# Key Takeaways

* `for` is used to iterate over an **iterable**.
* `range()` generates a sequence of integers for iteration.
* `range()` uses `start`, `stop`, and `step`.
* The `stop` value is **not included**.
* If `start` is omitted, it defaults to `0`.
* If `step` is omitted, it defaults to `1`.
* A negative `step` allows reverse iteration.
* A `for` loop can iterate through strings, lists, tuples, sets, dictionaries, ranges, and other iterables.
* `list(range())` converts the range into a list; it is not required for a `for` loop.

### Remember

> **For loop → Take one value → Execute the block → Take the next value → Repeat until the iterable is exhausted.**
