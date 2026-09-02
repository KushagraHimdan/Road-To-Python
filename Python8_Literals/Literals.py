# ================ numeric litrals =========

a = 0b1010 # binary litral
b = 100 # decimal litral
c = 0o310 # octal litral
d = 0x12c # hexadecimal litral

# float litrals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#  complex litrals
x = 3.14j

print(a, b, c, d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

# ============== String literals ===============

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001F600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# =================== Boolean Literals ================

x = True + 4
y = False + 10

print("a : ", x)
print("b : ", y)

# ===================== Special literals ============

z = None #kind of variable declaration
print(z)