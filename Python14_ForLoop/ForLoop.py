# ======================= For loop ==================

# range function -> provides integer values at a provided range

ls1 = list(range(1, 11))
print(ls1)

# if only one number is provided its the end number
# range(5) -> range(0, 5)
ls2 = list(range(11))
print(ls2)

# normal increment is of 1 unit but that can be changed by step parameter
ls3 = list(range(1, 11, 2))
print(ls3)

# Backword printing
ls4 = list(range(10, 0, -1))
print(ls4)

# ========= Sequence -> Things with order ==============
# ex : String, list, tuples, sets, dictionary

# for loop -> it can be implemented on range or sequence

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in "Kushagra":
    print(i)