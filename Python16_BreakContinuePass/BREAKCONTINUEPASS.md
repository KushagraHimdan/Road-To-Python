# Python `break`, `continue` & `pass`

Python provides three useful statements for controlling the execution of loops and blocks of code:

* `break`
* `continue`
* `pass`

Although they are often used together, they have **different purposes**.

---

# 1. `break`

The `break` statement **immediately terminates the loop** when a particular condition is satisfied.

### Example

```python id="z1q5vh"
# break -> at a specific condition break the loop

for i in range(1, 11):

    if i == 5:

        break

    print(i, end=" ")

print("")
```

### Output

```text id="5n4h8r"
1 2 3 4
```

### How it works

The loop starts:

```text id="r0i9kn"
i = 1 → print 1
i = 2 → print 2
i = 3 → print 3
i = 4 → print 4
i = 5 → break
```

When `i` becomes `5`, the `break` statement executes.

The loop **ends immediately**, so `5` and all values after it are not printed.

### Remember

> **`break` → Stop the entire loop.**

---

# 2. `continue`

The `continue` statement **skips the current iteration** and moves to the next iteration of the loop.

### Example

```python id="v6m0q2"
# continue -> no code will run for particular iteration

for i in range(1, 11):

    if i == 5:

        continue

    print(i, end=" ")

print("")
```

### Output

```text id="q1z7sx"
1 2 3 4 6 7 8 9 10
```

When `i` becomes `5`, `continue` is executed.

The remaining code in that iteration:

```python id="0l4p7x"
print(i, end=" ")
```

is skipped.

The loop then continues with `i = 6`.

### Execution

```text id="xk1q7s"
1 → print
2 → print
3 → print
4 → print
5 → skip
6 → print
7 → print
8 → print
9 → print
10 → print
```

### Remember

> **`continue` → Skip the current iteration and continue the loop.**

---

# 3. `pass`

The `pass` statement does **nothing**.

It is used as a placeholder when Python requires a statement, but you do not want to write the actual logic yet.

### Example

```python id="6r4b8m"
# pass -> if logic is not sure then use it to pass the statement

for i in range(1, 11):

    pass
```

This program produces no output.

The loop still executes 10 iterations, but `pass` does nothing during each iteration.

---

## Why Use `pass`?

Suppose you want to create a function but have not decided what logic to put inside it yet:

```python id="7f8n2p"
def calculate():
    pass
```

Without `pass`, Python would expect an indented statement inside the function.

You can add the actual logic later.

---

# Difference Between `break`, `continue` and `pass`

| Statement  | What it does                        |
| ---------- | ----------------------------------- |
| `break`    | Completely stops the loop           |
| `continue` | Skips the current iteration         |
| `pass`     | Does nothing; acts as a placeholder |

---

# Visual Comparison

Suppose:

```python id="1n4y6c"
for i in range(1, 6):
```

### `break`

```text id="yq1v9z"
1 → print
2 → print
3 → print
4 → print
5 → STOP LOOP
```

### `continue`

```text id="6m2p8r"
1 → print
2 → print
3 → print
4 → print
5 → SKIP
6 → print
```

### `pass`

```text id="3f8x2k"
1 → do nothing
2 → do nothing
3 → do nothing
4 → do nothing
5 → do nothing
```

---

# Important Difference

`break` and `continue` **change the normal flow of the loop**.

`pass` does **not** change the flow.

For example:

```python id="x5m2qs"
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

Output:

```text id="j8c1vw"
1
2
3
4
5
```

`pass` does nothing, so `3` is still printed.

If we use `continue`:

```python id="p3r7vz"
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text id="4q7n2k"
1
2
4
5
```

If we use `break`:

```python id="f6k9wd"
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

Output:

```text id="n8s4qp"
1
2
```

---

# Key Takeaways

* `break` **terminates the entire loop**.
* `continue` **skips only the current iteration**.
* `pass` **does nothing**.
* `pass` is useful as a placeholder for unfinished logic.
* `break` and `continue` are mainly used to control loop execution.
* `pass` does not skip an iteration or terminate a loop.

### Remember

> **break → Stop**
> **continue → Skip**
> **pass → Do nothing**
