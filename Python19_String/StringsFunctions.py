# ============== Strings Functions ===================

# len
k = "Kushagra"
print(len(k))

# max
print(max(k))

# min
print(min(k))

# sorted
print(sorted(k))
print(sorted(k, reverse=True))

# capitalize
k = "kushagra"
print(k.capitalize())

# title
k = "working on python"
print(k.title())

# upper
k = "kushagra"
print(k.upper())

# lower
k = "KUSHAGRA"
print(k.lower())

# swapcase
k = "KuSHagrA"
print(k.swapcase())

# count
k = "elephant elephant"
print(k.count('e'))
print(k.count('ele'))

# find / index

k = "kushagra"
print(k.find("a"))
print(k.find("m"))

k = "kushagra"
print(k.index("a"))
# print(k.index("a")) -> error

# endswith / startswith

k = "It is a good day"
print(k.endswith("ay"))

k = "It is a good day"
print(k.startswith("It"))

# format
k = "Hello my name is {} and I am {}"
print(k.format("Kushagra", 21))
k = "Hello my name is {1} and I am {0}"
print(k.format("Kushagra", 21))
k = "Hello my name is {name} and I am {age}"
print(k.format(name = "Kushagra", age = 21))

# isalnum / isalpha / isdecimal / isdigit / isidentifier
k = "Weight999"
print(k.isalnum())
k = "Weight"
print(k.isalpha())
k = "20"
print(k.isdigit())
k = "hello_kushagra"
print(k.isidentifier())

# split
k = "I am working on python"
print(k.split())
print(k.split("on"))

k = "-"
print(k.join(['I', 'am', 'working', 'on', 'python']))

# replace
k = "I am kushagra"
print(k.replace("kushagra", "lion"))

# strip
k = "           kushagra       "
print(k.strip())