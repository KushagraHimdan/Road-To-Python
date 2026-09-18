# =========== Important Built in Function ==============

# print
print("Hello World")

# input
input("Enter your Name : ")

# type
a = 5
type(a)

# type conversion
print(int('5')) # -> 5
print(int(5.9)) # -> 5

# abs
abs(4) # -> 4
abs(-4) # -> 4

# pow
pow(2, 3) # -> 2^3 = 8
pow(2, -3) # -> 2^(-3) = 0.125

# min / max
min([2, 5, 0, 1, 7]) # -> 0
max([2, 5, 0, 1, 7]) # -> 7

print(min("kushagra")) # -> a
print(max("kushagra")) # -> u

# round
pi = 22 / 7
print(round(pi, 3)) # -> round to 3 decimal places

# divmod -> reslt of integer division and modulos in a tuple
t = divmod(5, 2)
print(t)

# bin / oct / hex
a = bin(4)
print(a)

b = oct(16)
print(b)

c = hex(24)
print(c)

# id -> to get memory address of id
a = 7
print(id(a))

# ord -> Return the Unicode code point for a one-character string.
print(ord('K'))

# len
print(len("abcdefghijk"))

# sum
s = sum({2, 4, 5, 6 ,8})
print(s)

# help
help("print")