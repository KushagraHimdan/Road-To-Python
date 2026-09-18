# ================= Strings ============

# Strings are sequence of characters

# In Python specifically string are a sequence of unicode characters

# creating Strings
from regex import P
from sympy import StrPrinter


str = 'Kushagra'
print(str)

str = "It's good outside!!"
print(str)

str = '''Let's Play'''
print(str)

# Accessing substring from a string 

# indexing
str = "Kushagra"
print(str[4])

# positive indexing
print(str[7])
# negative indexing
print(str[-1])

# slicing 
str = "Hello World"
print(str[0:5])
print(str[2:])
print(str[:5])
# steps
print(str[0:5:2])
print(str[-5:-1:2])
# print(str[-5:-1:-2]) -> -ve step not allowed for +ve slice

print(str[::-1])
print(str[-1:-5:-1])

# Editing and Deleting in Strings
str = "Nice Food" # -> String are immutable

del str # not actully deleted 
print(str)

# ================ String operations ==============

str = "Kushagra"

# arithmetic operations
str2 = str + "!!"
print(str2)

str3 = str2 * 20
print(str3)

# relational operations
b = (str == str2)
print(b)
b = (str != str2)
print(b)
b = ("Kushagra" > "Lion") # lexiographically comparable
print(b)
b = ("lion" > "Lion") # ascii value
print(b)

# logical operations

# "" -> false (empty = false)
# "kushagra" -> true (non empty = true)

b = not "hello"
print(b)

b = not ""
print(b)

b = '' and "hello"
print(b)

b = '' or "hello"
print(b)

b = 'world' and "hello"
print(b)

b = 'world' or "hello"
print(b)


# loops
f = "Hello Kushagra"
for i in f:
    print(i, end=" ")
print()
# membership operations
m = "kushagra"
k = ("u" in m)
print(k)
k = ("K" in m)
print(k)
k = ("Z" not in m)
print(k)