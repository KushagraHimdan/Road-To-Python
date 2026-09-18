# Python Built-in Modules

## What is a Module?

A **module** is a Python file containing reusable code such as functions, classes, and variables.

It can be thought of as a **code library** that provides functionality which can be used in another Python program.

Python provides many modules as part of its **standard library**.

Some commonly used modules are:

* `math`
* `random`
* `os`
* `time`

---

# Importing a Module

To use a module, we generally import it using the `import` statement.

### Syntax

```python id="q8c5mk"
import module_name
```

After importing, its functions or values can be accessed using:

```python id="s2m9vx"
module_name.function()
```

---

# Python Standard Library

Python comes with a large collection of modules known as the **Python Standard Library**.

These modules provide ready-made functionality for tasks such as:

* Mathematical operations
* Random number generation
* File and directory operations
* Working with time
* Operating-system interaction
* Data handling
* Networking
* And many more

You can explore available modules using:

```python id="m7v2ka"
help("modules")
```

This can display a large list of modules available in your Python environment.

---

# 1. `math` Module

The `math` module provides mathematical functions and constants.

First, import it:

```python id="k3x9bp"
import math
```

### Examples

```python id="j6w4qs"
print(math.pi)

print(math.e)

print(math.factorial(5))

print(math.ceil(5.8))

print(math.floor(5.34))
```

### Explanation

#### `math.pi`

Provides the mathematical constant π.

```text id="8f2qtc"
3.141592653589793
```

#### `math.e`

Provides Euler's number.

```text id="x7k3mv"
2.718281828459045
```

#### `math.factorial()`

Calculates the factorial of a number.

```python id="4y8nqz"
math.factorial(5)
```

Result:

```text id="q5r8nt"
120
```

Because:

```text id="y1v7ch"
5! = 5 × 4 × 3 × 2 × 1 = 120
```

#### `math.ceil()`

Rounds a number **upward** to the nearest integer.

```python id="0h4w7p"
math.ceil(5.8)
```

Result:

```text id="a2j6kv"
6
```

#### `math.floor()`

Rounds a number **downward** to the nearest integer.

```python id="b8x5rd"
math.floor(5.34)
```

Result:

```text id="t6n2mw"
5
```

---

# 2. `random` Module

The `random` module provides functions for generating **pseudo-random** values.

Import it using:

```python id="v3q7ls"
import random
```

### Random Integer

```python id="f8k2mx"
print(random.randint(1, 100))
```

`randint(1, 100)` returns a random integer between `1` and `100`, **including both endpoints**.

For example:

```text id="n7p3cq"
57
```

The result can be different each time the program runs.

---

## `random.shuffle()`

`shuffle()` randomly rearranges the elements of a mutable sequence such as a list.

```python id="w4m8sz"
a = [1, 3, 5, 7, 9]

random.shuffle(a)

print(a)
```

Possible output:

```text id="j5x1qr"
[7, 1, 9, 3, 5]
```

The order can be different each time.

### Important

`shuffle()` modifies the original list rather than creating and returning a new shuffled list.

---

# 3. `time` Module

The `time` module provides functions related to time.

Import it using:

```python id="p6r2yb"
import time
```

### `time.time()`

```python id="z8c4nx"
print(time.time())
```

Returns the current time as the number of seconds since the **Unix epoch**.

The Unix epoch begins on:

```text
January 1, 1970, 00:00:00 UTC
```

---

### `time.ctime()`

```python id="q2v7mh"
print(time.ctime())
```

Returns the current time in a human-readable string format.

Example:

```text id="m9k3ds"
Fri Sep 18 20:15:30 2026
```

The exact output depends on the system's current date and time.

---

### `time.sleep()`

`time.sleep()` pauses program execution for a specified number of seconds.

```python id="r5x8kp"
print("hello")

time.sleep(1)

print("world")
```

Output:

```text id="c7m2vn"
hello
world
```

There is a **1-second delay** between the two outputs.

---

# 4. `os` Module

The `os` module provides functions for interacting with the **operating system**.

Import it using:

```python id="h6q9tw"
import os
```

### `os.getcwd()`

```python id="s3v7bx"
print(os.getcwd())
```

`getcwd()` means **Get Current Working Directory**.

It returns the directory from which the Python program is currently operating.

Example:

```text id="n4k8qp"
C:\Users\Kushagra\Python
```

The actual path depends on your system.

---

### `os.listdir()`

```python id="x9m5cr"
print(os.listdir())
```

Returns a list containing the names of files and directories in the current working directory.

Example:

```text id="f7w2mz"
['main.py', 'README.md', 'notes']
```

The output depends on the contents of the current directory.

---

# Complete Example

```python id="k8v3pq"
# ============ Built in Module ================

# Module can be considered as a code library

# A file containing a set of function you want to include in your application

# Example of Python modules:
# math
# random
# os
# time

# help("modules")

# math

import math

print(math.pi)

print(math.e)

print(math.factorial(5))

print(math.ceil(5.8))

print(math.floor(5.34))

# random

import random

print(random.randint(1, 100))

a = [1, 3, 5, 7, 9]

random.shuffle(a)

print(a)

# time

import time

print(time.time())

print(time.ctime())

print("hello")

time.sleep(1)

print("world")

# os

import os

print(os.getcwd())

print(os.listdir())
```

---

# Module vs Library vs Package

These terms are related but are not exactly the same.

| Term        | Meaning                                                |
| ----------- | ------------------------------------------------------ |
| **Module**  | Usually a single Python file containing reusable code  |
| **Package** | A directory containing related Python modules          |
| **Library** | A broader collection of reusable code/modules/packages |

For example:

```text
Module → math
Package → collection of related modules
Library → collection of reusable functionality
```

In everyday Python discussions, the terms can sometimes be used loosely.

---

# Why Use Modules?

Modules help us:

* Reuse existing code
* Avoid writing the same functionality repeatedly
* Organize large programs
* Keep code easier to maintain
* Access Python's extensive standard library
* Add functionality without implementing everything from scratch

---

# Key Takeaways

* A **module** is a reusable unit of Python code, commonly a `.py` file.
* Python provides many modules through its **standard library**.
* Use `import` to bring a module into your program.
* `math` provides mathematical functions and constants.
* `random` provides pseudo-random operations.
* `time` provides time-related functionality.
* `os` provides operating-system-related functionality.
* `help("modules")` can be used to explore modules available in the environment.
* Modules make programs more **organized, reusable, and maintainable**.

### Remember

> **Import → Access → Use**

```python
import math

print(math.pi)
```

Here, `math` is imported first, and then `pi` is accessed through the module.
