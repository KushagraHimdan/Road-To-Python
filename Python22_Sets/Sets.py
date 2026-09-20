# ================ Sets ===============

# Rules of sets
# 1. Sets don't allow duplicates
# 2. Sets don't have indexing/slicing
# 3. Sets don't allow mutable data types
# 4. Sets itself is a mutable data types

# crate

# empty set
s = set()
print(s)
print(type(s))

# homogenous set
s = {1, 2, 3, 4}
print(s)

# hetrogenous set
s = {1, 2.2, "True", "Kushagra"}
print(s)

# Sets don't allow duplicates
s = {1, 1, 2, 3, 3, 4, 5, 5}
print(s) # -> {1, 2, 3, 4, 5}

# Sets don't allow mutable data types

# s = {[1, 2, 3], "Kushagra"} -> list is mutable so erro
s = {(1, 2, 3), "Kushagra"}
print(s)
# In sets order can differ from orignal because they don't follow indexing the follow hashing

# Sets don't have indexing/slicing
s = {1, 1, 2, 3, 3, 4, 5, 5}
# print(s[0]) -> set object does not suport indexing and slicing

# Sets itself is a mutable data types
# add items
s = {1, 1, 2, 3, 3, 4, 5, 5}
s.add(8)
print(s)

# delete

# del
s = {1, 1, 2, 3, 3, 4, 5, 5}
del s

# remove
s = {1, 1, 2, 3, 3, 4, 5, 5}
s.remove(5)
print(s)

# pop
s = {1, 1, 2, 3, 3, 4, 5, 5}
s.pop() # because of hashing 1 will be removed
print(s) 

# operations
s = {1, 2, 3, 4, 5}

for i in s:
    print(i)

# membership
print(1 in s)

# functions
s = {1, 2, 3, 4, 5}
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(sorted(s))
print(sorted(s, reverse=True))

s1 = {1, 2, 4, 6, 9, 7}
s2 = {2, 3, 5, 10, 1, 8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
s1.clear()
print(s1)