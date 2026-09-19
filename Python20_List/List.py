# ==================== List ========================

# list -> list is a datatype use to store heterogeneous datatype

# Array v/s List -> 
# Array stores homogenous data but list can be heterogeneous
# Array has Continuous memory allocation but not in the list
# Arrays are much faster than list
# list are more programmer friendly

# create list
from cv2 import sort


l = []

# homogenous list
l = [1, 2, 3, 4, 5]
print(l)

# heterogeneous list
l = [1, 3.4, "kushagra", True, 5+6j]
print(l)

# multi-dimensional list

# 2D list -> 
l = [12, 14, [23, 45]]
print(l)
# 3D list -> 
l = [[[1,2], [3, 4]],[[5, 6], [6, 7]]]
print(l)
l = list("Kushgara")
print(l)

# access data from list
l = [1, 3.4, "kushagra", True, 5+6j]
print(l[2])
print(l[2:4])
print(l[::-1])

l = [12, 14, [23, 45]]
print(l[-1])
print(l[2][1])
print(l[-1][1])

l = [[[1,2], [3, 4, 7]],[[5, 6], [6, 7]]]
print(l[0][1][2])

# edit -> list in python are mutable
l = [1, 2, 3, 4, 5]
l[2] = 12
print(l)
l[1:4] = [200, 300,400]
print(l)

# add item -> 
# append -> add 1 item
l = [1, 3.4, "kushagra", True, 5+6j]
l.append(190)
print(l)
l.append([190, "Tiger"])

# extend -> add multiple item
l.extend(["Lion", 499])
print(l)
l.extend("Laptop")
print(l)

# insert -> add btw element
l = [1, 3.4, "kushagra", True, 5+6j]
l.insert(4, "Lion")
print(l)

# delete ->
# del
l = [1, 3.4, "kushagra", True, 5+6j]
del l # -> delete list

l = [1, 3.4, "kushagra", True, 5+6j]
del l[-1]
print(l)

# remove
l = [1, 3.4, "kushagra", True, 5+6j]
l.remove(3.4)
print(l)

# pop
l = [1, 3.4, "kushagra", True, 5+6j]
l.pop()
print(l)

# clear
l = [1, 3.4, "kushagra", True, 5+6j]
l.clear()
print(l)


# operations
l = [1, 2, 3, 4, 5]
m = [10, 11, 12, 13]

# add
k = l + m
print(k)
# multiply
k = l * 3
print(k)

for i in l:
    print(i)

# membership
print(3 in l)

# functions
l = [1, 2, 3, 4, 5]
m = len(l)
print(m)
print(min(l))
print(max(l))

l = [1, 9, 3, 7, 5]
print(sorted(l))
print(sorted(l, reverse=True))
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l = [1, 9, 3, 7, 5]
print(l.index(9))

