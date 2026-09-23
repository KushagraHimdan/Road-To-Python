# ================= Varables and Memory References ===============

a = 4 
print(id(a))
print(id(4))
# python call a the name
# the a will start pointing to the memory space "starting address"
# this is called call by object reference


# Aliasing
a = 5
b = a
print(id(a))
print(id(b))
# a is pointing to some memory address
# b is pointing to same memory address
# if we delete a, b will still point to same memory address
# Here the reference of a is deleted but b remains

a = 5
b = a
a = 6
print(b)
# here the b pointer still points to memory address of 5

# Reference Counting 
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

# Garbage Collection
a = 9
b = a
c = b
del a
del b
del c
# now no one is pointing to 9 only the references are deleted
# Then garbage collection an internal program runs periodically to free any memory which is being used but not getting pointed
# It will free up the memory for other computations

# ========== Python Behaviour ========

# 1. for pointing 2
a = 2
b = a
c = b

print(sys.getrefcount(a))
# two is a very common number so it has multiple other internal references thus giving a random number of internal references

# 2. 
a = 4
b = 4
print(id(a))
print(id(b))

a = 533
b = 533
print(id(a))
print(id(b))
# python creates some cells for frequently used numbers 

# 3.
a = "kush"
b = "kush"
print(id(a))
print(id(b))
a = "kush eating food"
b = "kush eating food"
print(id(a))
print(id(b))
a = "kush_eating_food"
b = "kush_eating_food"
print(id(a))
print(id(b))

# list
l = [1, 2, 3]
print(id(l))
print(id(1))
print(id(l[0]))
# both l[0] and 1 are pointing to same point
# l created a memory sapce storing 3 addresses they all are pointing to memory space where 1, 2, 3 exist
l[2] = 1
print(id(l[2]))

l = [1, 2, 3, [4, 5]]
# here l have 4 spaces pointing to different spaces one of them itself is a list containing real address of the values


# =========== Mutability ===========
# it refers to the ability to change or edit data in it's memory location

# immutable datatype -> string, int, float, bool, complex, tuple
# mutable -> list, dictionary, sets

a = "hello"
print(a)
print(id(a))
a = a + "world"
print(a)
print(id(a))
# here the memory location of a has changed meaning a completly new string is created pointed by a

t = (1, 2, 4)
print(t)
print(id(t))
t = t + (8, 9)
print(t)
print(id(t))
# here as well the memory location has changed 

l = [1, 3, 5]
print(l)
print(id(l))
l.append(9)
print(l)
print(id(l))
# here the memory location remain same

# side effect of mutability

l = [1, 2, 3, 4]
print(id(l))
l1 = l
print(id(l1))
l.append(1)
print(l)
print(l1)
print(id(l))
print(id(l1))
# here the change in l1 led to change in l

# how to handle it
# ===== cloning ===========
l = [1, 2, 3, 4]
l1 = l[:]
print(id(l))
print(id(l1))
l1.append(9)
print(l)
print(l1)

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