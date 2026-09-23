# Python Variables and Memory References

In Python, a variable does not directly contain a value in the way it is often imagined.

Instead, a variable is a **name/reference** that points to an object stored in memory.

A useful mental model is:

```text
Variable → Object
```

For example:

```python
a = 4
```

Conceptually:

```text
a ───────→ 4
```

Here:

* `a` is the variable/name.
* `4` is an integer object.
* `a` refers to the object `4`.

---

# 1. Variables and Memory References

```python
a = 4

print(id(a))

print(id(4))
```

The two `id()` calls will normally produce the same identity for this object.

This demonstrates that `a` refers to the integer object `4`.

```text
a ───────→ 4
```

### Important terminology

Python variables are often described as **names bound to objects**.

The variable `a` is not the memory location itself.

Instead:

```text
a → reference to an object
```

The `id()` function returns an integer that identifies the object during its lifetime.

---

# 2. Python Uses Object References

Python uses a model commonly described as **call by object reference** or **call by sharing**.

The important idea is:

```text
Variables refer to objects.
```

For example:

```python
a = 4
```

Conceptually:

```text
a ─────→ 4
```

If another variable refers to the same object:

```python
b = a
```

then:

```text
a ─────→ 4
b ─────→ 4
```

Both names refer to the same object.

---

# 3. Aliasing

**Aliasing** means that multiple variables refer to the same object.

```python
a = 5

b = a

print(id(a))

print(id(b))
```

Both variables refer to the same object.

Conceptually:

```text
       ┌────→ 5
a ─────┤
b ─────┘
```

Therefore:

```python
a is b
```

would return:

```text
True
```

because both names refer to the same object.

---

# 4. Reassigning One Variable

Consider:

```python
a = 5

b = a

a = 6

print(b)
```

Output:

```text
5
```

Why?

Initially:

```text
a ─────→ 5
b ─────→ 5
```

After:

```python
a = 6
```

the name `a` is simply rebound:

```text
a ─────→ 6

b ─────→ 5
```

Changing what `a` refers to does not change what `b` refers to.

### Important

```text
Reassignment ≠ modifying the object
```

You changed the reference held by `a`; you did not modify the integer object `5`.

---

# 5. Reference Counting

Python keeps track of how many references point to objects.

The `sys` module provides `getrefcount()`:

```python
import sys

a = "kushagra"

b = a

c = b

print(id(a))

print(id(b))

print(id(c))

print(sys.getrefcount(a))

print(a is b)

print(b is c)
```

Conceptually:

```text
a ─────┐
b ─────┼──→ "kushagra"
c ─────┘
```

Therefore:

```python
a is b
```

returns:

```text
True
```

and:

```python
b is c
```

also returns:

```text
True
```

---

## Important Note About `getrefcount()`

`sys.getrefcount(a)` itself temporarily creates an additional reference while the function is being called.

Therefore, the number returned by:

```python
sys.getrefcount(a)
```

can be one higher than the number you might expect from the visible variables.

Also, Python implementations can have other internal references.

So do **not** use `getrefcount()` as a simple way to count only the variables you created.

---

# 6. Garbage Collection

Consider:

```python
a = 9

b = a

c = b

del a

del b

del c
```

Initially:

```text
a ─────┐
b ─────┼──→ 9
c ─────┘
```

After:

```python
del a
del b
del c
```

none of these names refer to the object anymore.

Conceptually:

```text
No reference → 9
```

When an object is no longer reachable, Python can reclaim the memory associated with it.

Python also has a **garbage collector** that handles certain kinds of unreachable objects, particularly reference cycles.

### Important distinction

Python's memory management is not simply:

```text
No reference → garbage collector immediately deletes it
```

In CPython, reference counting often causes objects to be reclaimed immediately when their reference count reaches zero, while the cyclic garbage collector handles reference cycles.

For beginner-level understanding:

```text
No longer reachable object → memory can eventually be reclaimed
```

---

# 7. Python Behaviour With Common Objects

Python may reuse certain objects.

This means that two variables containing the same value may sometimes refer to the same object.

However, you should **never rely on `id()` equality for ordinary value comparison**.

Use:

```python
==
```

to compare values.

Use:

```python
is
```

to check object identity.

---

# 8. Integer Object Reuse

```python
a = 2

b = a

c = b

print(sys.getrefcount(a))
```

The integer `2` can have many references because Python commonly reuses objects for certain small integers.

Therefore, the reference count can be larger than the references that you explicitly created.

---

# 9. Same Integer Values

```python
a = 4

b = 4

print(id(a))

print(id(b))
```

Python may make both names refer to the same integer object.

Conceptually:

```text
a ─────┐
       ├──→ 4
b ─────┘
```

Now:

```python
a = 533
b = 533

print(id(a))

print(id(b))
```

Depending on the Python implementation and execution context, Python may also reuse the same object here.

### Important

Do not build logic around this behavior.

For values:

```python
a == b
```

is the correct comparison.

For identity:

```python
a is b
```

checks whether they are the same object.

---

# 10. String Object Reuse

Consider:

```python
a = "kush"

b = "kush"

print(id(a))

print(id(b))
```

Python may reuse the same string object.

Now:

```python
a = "kush eating food"

b = "kush eating food"

print(id(a))

print(id(b))
```

Again, Python may reuse the same object.

Another example:

```python
a = "kush_eating_food"

b = "kush_eating_food"

print(id(a))

print(id(b))
```

The same object may be reused.

This is related to Python's implementation optimizations such as **interning**.

### Important

Do not assume:

```python
same value → same id
```

or:

```python
different spelling → different id
```

Object identity is an implementation/runtime detail.

Use:

```python
==
```

when you care about values.

---

# 11. Lists and References

Consider:

```python
l = [1, 2, 3]

print(id(l))

print(id(1))

print(id(l[0]))
```

`l` is a list object.

Conceptually, the list contains references to its elements:

```text
l
│
├──→ 1
├──→ 2
└──→ 3
```

Therefore:

```python
id(l[0])
```

and:

```python
id(1)
```

can refer to the same integer object.

The important mental model is:

```text
List
  ↓
references to objects
```

The list does not necessarily contain independent copies of the values.

---

# 12. Changing a List Element

```python
l[2] = 1

print(id(l[2]))
```

Now the third position refers to the object `1`.

Conceptually:

```text
l
│
├──→ 1
├──→ 2
└──→ 1
```

The list contains references to objects.

---

# 13. Nested Lists

```python
l = [1, 2, 3, [4, 5]]
```

Here the list contains four references:

```text
l
│
├──→ 1
├──→ 2
├──→ 3
└──→ [4, 5]
        │
        ├──→ 4
        └──→ 5
```

The fourth element is itself another list object.

This is called a **nested list**.

---

# Mutability

**Mutability** refers to whether an object's contents can be changed after the object has been created.

There are two important categories:

```text
Immutable → Object cannot be modified after creation
Mutable   → Object can be modified after creation
```

---

# 14. Immutable Data Types

Common immutable Python data types include:

```text
int
float
bool
complex
str
tuple
```

For these objects, an operation that appears to modify the value actually creates or refers to another object.

---

# 15. Mutable Data Types

Common mutable Python data types include:

```text
list
dictionary
set
```

Their contents can be changed without creating an entirely new object for every modification.

---

# 16. String Mutability

Consider:

```python
a = "hello"

print(a)

print(id(a))

a = a + "world"

print(a)

print(id(a))
```

The string is immutable.

When:

```python
a = a + "world"
```

is executed, Python creates a new string object.

Conceptually:

```text
Before:

a ─────→ "hello"


After:

a ─────→ "helloworld"
```

The original string `"hello"` was not modified.

The name `a` was rebound to another string object.

This is why the identity can change.

---

# 17. Tuple Mutability

Consider:

```python
t = (1, 2, 4)

print(t)

print(id(t))

t = t + (8, 9)

print(t)

print(id(t))
```

Tuples are immutable.

Therefore, the original tuple cannot be modified.

Instead, a new tuple is created:

```text
Before:

t ─────→ (1, 2, 4)


After:

t ─────→ (1, 2, 4, 8, 9)
```

The identity changes because a new tuple object is created.

---

# 18. List Mutability

Consider:

```python
l = [1, 3, 5]

print(l)

print(id(l))

l.append(9)

print(l)

print(id(l))
```

The list is mutable.

`append()` modifies the existing list object.

Conceptually:

```text
Before:

l ─────→ [1, 3, 5]


After:

l ─────→ [1, 3, 5, 9]
```

The list object itself remains the same.

Therefore, its `id()` remains the same.

---

# 19. Side Effect of Mutability

Mutability becomes especially important when multiple variables refer to the same mutable object.

Consider:

```python
l = [1, 2, 3, 4]

print(id(l))

l1 = l

print(id(l1))

l.append(1)

print(l)

print(l1)

print(id(l))

print(id(l1))
```

Initially:

```text
l  ─────┐
        ├──→ [1, 2, 3, 4]
l1 ─────┘
```

Both names refer to the same list.

When:

```python
l.append(1)
```

the existing list is modified.

Therefore, both variables see the change:

```text
l  ─────┐
        ├──→ [1, 2, 3, 4, 1]
l1 ─────┘
```

So:

```python
print(l)
print(l1)
```

both show:

```text
[1, 2, 3, 4, 1]
```

### Important

This is called **aliasing**.

```text
l1 = l
```

does not create a copy.

It creates another reference to the same list.

---

# 20. Cloning a List

If you want a separate list, you can create a copy.

One simple method is slicing:

```python
l = [1, 2, 3, 4]

l1 = l[:]

print(id(l))

print(id(l1))

l1.append(9)

print(l)

print(l1)
```

Now:

```text
l  ─────→ [1, 2, 3, 4]

l1 ─────→ [1, 2, 3, 4]
```

They are separate list objects.

Therefore, changing `l1` does not change `l`.

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4, 9]
```

### Important

This creates a **shallow copy**.

For simple lists, this is often enough.

---

# 21. Shallow Copy and Nested Objects

Consider:

```python
a = [1, 2]

b = [3, 4]

c = (a, b)

print(c)

print(id(a))

print(id(b))

print(id(c))

c[1][1] = 5

print(c)

print(id(a))

print(id(c))
```

Here:

```text
c
│
├──→ a → [1, 2]
│
└──→ b → [3, 4]
```

The tuple `c` is immutable, but it contains references to mutable lists.

Therefore:

```python
c[1][1] = 5
```

is allowed.

Why?

You are **not replacing an element of the tuple**.

Instead, you are modifying the list stored inside the tuple.

The result becomes:

```text
([1, 2], [3, 5])
```

This gives an important concept:

```text
Immutable container
        ↓
Can contain mutable objects
        ↓
Those mutable objects can still be changed
```

So:

```python
c[1] = [3, 5]
```

would be invalid because that attempts to change the tuple itself.

But:

```python
c[1][1] = 5
```

is valid because it modifies the mutable list inside the tuple.

---

# 22. Mutable vs Immutable

## Immutable

```text
int
float
bool
complex
str
tuple
```

Their contents cannot be changed after creation.

Operations that appear to modify them generally create another object.

---

## Mutable

```text
list
dict
set
```

Their contents can be changed after creation.

---

# 23. Reassignment vs Mutation

This is one of the most important distinctions in Python.

### Reassignment

```python
a = 5

a = 6
```

The name `a` is now bound to another object.

```text
a ─→ 5

      ↓ reassignment

a ─→ 6
```

---

### Mutation

```python
l = [1, 2, 3]

l.append(4)
```

The same list object is modified.

```text
l ─→ [1, 2, 3]

      ↓ mutation

l ─→ [1, 2, 3, 4]
```

### Easy way to remember

```text
Reassignment → changes what the variable refers to
Mutation     → changes the mutable object itself
```

---

# 24. `is` vs `==`

These concepts are closely related to memory references.

## `==`

Checks whether two objects have equal values.

```python
a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

The contents are equal.

---

## `is`

Checks whether two names refer to the **same object**.

```python
print(a is b)
```

Output:

```text
False
```

because `a` and `b` are separate list objects.

Conceptually:

```text
a ─→ [1, 2, 3]

b ─→ [1, 2, 3]
```

Same value, different objects.

### Easy rule

```text
==  → Same value?
is  → Same object?
```

For normal value comparison, use `==`.

---

# 25. Complete Mental Model

A useful way to visualize Python variables is:

```text
Variable / Name
       │
       ↓
    Object
       │
       ↓
   Data / Value
```

For mutable objects:

```text
a ─────┐
       ↓
    [1, 2, 3]
       ↑
       └───── b
```

If `a` and `b` refer to the same list, changing the list through one reference is visible through the other.

For immutable objects:

```text
a ─→ "hello"
```

An operation that creates a different value results in a new object rather than modifying the existing string.

---

# Important Points to Remember

* Python variables are **names bound to objects**.
* A variable does not simply contain the value itself.
* `id()` gives an identity associated with an object during its lifetime.
* Multiple variables can refer to the same object.
* This is called **aliasing**.
* `a = b` does not copy the object.
* Reassigning one variable does not automatically affect another variable.
* Mutable objects can be modified in place.
* Immutable objects cannot be modified in place.
* `list`, `dict`, and `set` are mutable.
* `int`, `float`, `bool`, `complex`, `str`, and `tuple` are immutable.
* `del` removes a name/reference; it does not mean "manually erase this value from memory."
* When an object becomes unreachable, Python can reclaim its memory.
* CPython commonly uses reference counting and also has a cyclic garbage collector.
* `sys.getrefcount()` includes a temporary reference created by the function call.
* Python may reuse objects, especially commonly used immutable objects.
* Never rely on `id()` behavior for normal program logic.
* Use `==` to compare values.
* Use `is` to compare object identity.
* `l1 = l` creates an alias, not a copy.
* `l1 = l[:]` creates a shallow copy of a list.
* A tuple can contain mutable objects, and those objects can still be modified.
* **Reassignment changes the reference; mutation changes the mutable object.**

---

# Quick Revision

```text
Variable
   ↓
Reference / Binding
   ↓
Object
```

```text
Aliasing
a = [1, 2]
b = a

a ───┐
     ├──→ [1, 2]
b ───┘
```

```text
Reassignment
a = 5
a = 6

a ─→ 6
```

```text
Mutation
l = [1, 2]
l.append(3)

Same list object → [1, 2, 3]
```

```text
Comparison
== → value equality
is → object identity
```

```text
Immutable → int, float, bool, complex, str, tuple
Mutable   → list, dict, set
```
