# =================== Arithmetic operation =============
a = 5
b = 2

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a % b) # modulo
print(a ** b) # power of
print(a // b) # integer division

# ==================== Comparision operation ==============

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# ===================== logical operation ===============

x = True
y = False

print(x or y)
print(x and y)
print(not x)
print(not y)

# ================== Bitwise operation =============

m = 2
n = 3

print(m & n)
print(m | n)
print(m >> 2)
print(n << 2)
print(~m)

# ========= Assignment operation ================
k = 3
print(k)
k+=4
print(k)
k-=2
print(k)
k*=3
print(k)
k&=2
print(k)
# python don have pre or post increment ++k or k++

# ============== identity operators =============
# check if two varibles are at same memory location
p = 5
q = 5
print(p is q) # -> true

p = "Hello"
q = "Hello"
print(p is q) # -> true

p = [1, 2, 3]
q = [1, 2, 3]
print(p is q) # -> false

p = "Hello-world"
q = "Hello-world"
print(p is not q) # -> false

# ============= Membership operator ================

h = "Delhi"
print("D" in h)
print("D" not in h)

h = [1, 2, 3]
print(1 in h)
print(5 in h)
# applicable on list tuple dictionary sets
