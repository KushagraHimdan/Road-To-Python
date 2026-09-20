# ================ Tuples ================

# Tuples -> 

# create 
t = ()

# homogenous tuple
t = (1, 2, 3, 4, 5)
print(t)

# hetrogenous tuple
t = (2, "kushagra", True, 9.1)
print(t)

# 2D / 3D
t = (1, 2, 3, (11, 22))
print(t)
t = ((1, (2, 3)), (11, 22))
print(t)

# we can't make single element tuple implecitly
t = (1)
print(type(t)) # -> int

# making a single element tuple
t = (1,)
print(t)
print(type(t))

# type conversion
t = tuple("kushagra")
print(t)
t = tuple([1, 2, 3, 4])
print(t)

# access
t = (2, "kushagra", True, 9.1)
print(t[1])
print(t[-1])
print(t[:3])

t = (1, 2, 3, (11, 22))
print(t[3][-1])

#  tuple v/s list
# tuples are immutable but list are mutable
# we can't add more elements to the tuple if once made
# tuples are read only datatype
# delete
t = (1, 2, 3, (11, 22))
del t

# operations
t = (1, 2, 3, (11, 22))
t2 = t + t
print(t2)
t2 = t * 3
print(t2)

t = (1, 2, 3, (11, 22))

for i in t:
    print(i)


# membership
t = (1, 2, 3, (11, 22))
print((11, 22) in t)

# function
t = (1, 2, 3, 4, 5)
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t))
print(sorted(t, reverse=True))