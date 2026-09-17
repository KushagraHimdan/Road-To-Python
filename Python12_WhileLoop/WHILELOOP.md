# Python While Loop

## What is a While Loop?

A **while loop** is an **iteration control statement** used to repeatedly execute a block of code as long as a given condition is `True`.

### Basic Syntax

```python
while condition:
    # code to execute
```

The loop:

1. Checks the condition.
2. If the condition is `True`, executes the code inside the loop.
3. Updates the required variable.
4. Checks the condition again.
5. Stops when the condition becomes `False`.

---

## Example: Printing a Table

```python
#================== While Loop -> Iteration Control block =============

# printing table

number = int(input("Enter the number : "))

i = 1

while i < 11:

    print(number, "*", i, "=", number * i)

    i += 1
```

### Example Output

If the user enters:

```text
Enter the number : 5
```

Output:

```text
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```

---

## Understanding the Example

### 1. Take input

```python
number = int(input("Enter the number : "))
```

`input()` takes the value as a string, so `int()` converts it into an integer.

For example:

```text
5 → 5
```

---

### 2. Initialize the counter

```python
i = 1
```

The variable `i` is used as the multiplier.

It starts from `1`.

---

### 3. Set the loop condition

```python
while i < 11:
```

The loop continues while `i` is less than `11`.

Therefore, the values of `i` will be:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

---

### 4. Execute the loop body

```python
print(number, "*", i, "=", number * i)
```

This prints the multiplication table.

For example, when:

```python
number = 5
i = 3
```

The output is:

```text
5 * 3 = 15
```

---

### 5. Update the counter

```python
i += 1
```

This increases `i` by `1`.

It is equivalent to:

```python
i = i + 1
```

Without this update, `i` would remain `1`, the condition would remain `True`, and the loop could become an **infinite loop**.

---

## Loop Execution Flow

For `number = 5`:

```text
i = 1
   ↓
1 < 11 → True
   ↓
5 * 1 = 5
   ↓
i = 2
   ↓
2 < 11 → True
   ↓
5 * 2 = 10
   ↓
...
   ↓
i = 10
   ↓
10 < 11 → True
   ↓
5 * 10 = 50
   ↓
i = 11
   ↓
11 < 11 → False
   ↓
Loop ends
```

---

## Important Parts of a While Loop

A typical `while` loop has three important parts:

```python
i = 1                  # Initialization

while i <= 10:         # Condition
    print(i)
    i += 1             # Update
```

| Part           | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| Initialization | Gives the loop variable its starting value                |
| Condition      | Decides whether the loop should continue                  |
| Update         | Changes the loop variable so the loop can eventually stop |

---

## Infinite Loop

If the loop condition never becomes `False`, the loop continues indefinitely.

Example:

```python
i = 1

while i <= 10:
    print(i)
```

Here, `i` is never updated, so it always remains `1`.

Therefore:

```text
1
1
1
1
...
```

This is called an **infinite loop**.

---

## While Loop vs For Loop

| While Loop                                         | For Loop                                                 |
| -------------------------------------------------- | -------------------------------------------------------- |
| Used when repetition depends mainly on a condition | Often used when iterating over a sequence or known range |
| Condition is checked each iteration                | Iterates through items/range                             |
| Requires careful initialization and updating       | Usually handles iteration automatically                  |
| Can easily create an infinite loop                 | Less likely to accidentally become infinite              |

Example:

```python
# while loop
i = 1

while i <= 5:
    print(i)
    i += 1
```

```python
# for loop
for i in range(1, 6):
    print(i)
```

---

## Key Takeaways

* `while` is used for **repeated execution** based on a condition.
* The condition is checked before every iteration.
* The loop body must be properly indented.
* The loop variable should usually be updated inside the loop.
* `i += 1` is commonly used to move toward the stopping condition.
* If the condition never becomes `False`, an infinite loop can occur.

### Remember

> **Initialize → Check Condition → Execute → Update → Repeat**
