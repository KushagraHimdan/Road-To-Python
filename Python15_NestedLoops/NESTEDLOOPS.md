# Python Nested Loops

## What is a Nested Loop?

A **nested loop** is a loop placed inside another loop.

The outer loop controls the larger repetition, while the inner loop executes completely for each iteration of the outer loop.

### Basic Structure

```python
for i in range(...):
    for j in range(...):
        # inner loop code
```

For every single iteration of the **outer loop**, the **inner loop runs from beginning to end**.

---

# Example: Printing a Triangle

```python id="v4h2km"
# ========== Nested Loops =============

# Print pascal triangle

rows = int(input("Enter the number of rows : "))

for i in range(1, rows + 1):

    for j in range(0, i):

        print("*", end=" ")

    print("")
```

> **Note:** This program prints a **star triangle**. It demonstrates nested loops, but it is not the numerical Pascal's Triangle.

---

## Example Output

If the user enters:

```text
Enter the number of rows : 5
```

Output:

```text
* 
* * 
* * * 
* * * * 
* * * * * 
```

---

# Understanding the Code

## 1. Take the Number of Rows

```python
rows = int(input("Enter the number of rows : "))
```

The user enters how many rows should be printed.

For example:

```text
rows = 5
```

---

## 2. Outer Loop

```python
for i in range(1, rows + 1):
```

The outer loop controls the **number of rows**.

If:

```text
rows = 5
```

then:

```python
range(1, 6)
```

produces:

```text
1, 2, 3, 4, 5
```

Therefore, the outer loop runs **5 times**.

---

## 3. Inner Loop

```python
for j in range(0, i):
```

The inner loop controls the **number of stars in each row**.

The value of `i` changes with every outer-loop iteration.

| Outer `i` | Inner range   | Number of stars |
| --------: | ------------- | --------------: |
|         1 | `range(0, 1)` |               1 |
|         2 | `range(0, 2)` |               2 |
|         3 | `range(0, 3)` |               3 |
|         4 | `range(0, 4)` |               4 |
|         5 | `range(0, 5)` |               5 |

So the number of stars increases by one in every row.

---

# How Nested Loops Execute

Suppose:

```text
rows = 3
```

### First outer iteration

```text
i = 1
```

Inner loop:

```python
range(0, 1)
```

Runs once:

```text
*
```

---

### Second outer iteration

```text
i = 2
```

Inner loop:

```python
range(0, 2)
```

Runs twice:

```text
* *
```

---

### Third outer iteration

```text
i = 3
```

Inner loop:

```python
range(0, 3)
```

Runs three times:

```text
* * *
```

Final output:

```text
*
* *
* * *
```

---

# Understanding `end=" "`

Normally:

```python
print("*")
```

prints the value and moves to the next line.

But:

```python
print("*", end=" ")
```

prints the value and **stays on the same line**.

Therefore, the inner loop can print multiple stars on the same row.

Example:

```python
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
```

Output:

```text
* * *
```

---

# Understanding `print("")`

After the inner loop finishes:

```python
print("")
```

moves the cursor to the next line.

This allows the next iteration of the outer loop to start a new row.

Without it, all stars would be printed on the same line.

---

# Execution Pattern

For `rows = 5`:

```text
Outer Loop
│
├── i = 1
│   └── Inner loop → 1 star
│
├── i = 2
│   └── Inner loop → 2 stars
│
├── i = 3
│   └── Inner loop → 3 stars
│
├── i = 4
│   └── Inner loop → 4 stars
│
└── i = 5
    └── Inner loop → 5 stars
```

The important idea is:

> **The inner loop completes all its iterations for every single iteration of the outer loop.**

---

# Nested Loop Example

Nested loops are not limited to patterns.

They can be used for working with:

* Patterns
* Tables
* Matrices
* 2D lists
* Grids
* Combinations
* Searching through nested data

Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

For each value of `i`, the inner loop runs completely through all values of `j`.

---

# Nested Loop vs Single Loop

### Single Loop

```python
for i in range(1, 6):
    print(i)
```

One loop controls one repetition.

### Nested Loop

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
```

The second loop runs repeatedly inside the first loop.

---

# Key Takeaways

* A **nested loop** is a loop inside another loop.
* The **outer loop** controls the larger repetition.
* The **inner loop** runs completely for every iteration of the outer loop.
* Nested loops are commonly used for patterns, matrices, grids, and nested data.
* `end=" "` keeps printing on the same line.
* `print("")` moves to the next line.
* In the given example, the outer loop controls **rows**, while the inner loop controls **stars per row**.

### Remember

> **Outer loop → controls rows/repetitions**
> **Inner loop → controls work inside each repetition**
