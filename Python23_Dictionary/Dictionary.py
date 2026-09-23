# ================= Dictionary ==================
# Rules
# 1. Dictionaryhas no indexing
# 2. Dictionary is a mutable datatype
# 3. keys are immutable || values can be mutable
# 4. keys should be unique

# create
d = {}
print(d)

d = {"name":"kushagra", "age":21}
print(d)

# keys are immutable || values can be mutable
# d = {[1, 2]:"kushagra", "age":21} -> error list are mutable
d = {(1, 2):"kushagra", "age":21} 
print(d)

# keys should be unique
d = {1:"Apple", 2:"Ball", 3:"Cat"}
print(d)
d = {1:"Apple", 2:"Ball", 1:"Cat"}
print(d) # -> {1: 'Cat', 2: 'Ball'}
# so the value for same key is updated

# 2D dictionary
d = {"Name":"Kushagra", "Language":"Python", "Marks":{"A":45, "B":48, "C": 50}}
print(d)

# access
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
print(d)

# Dictionaryhas no indexing
# provide current key
print(d[2])
# for 1D dictionary
print(d.get(5))

d = {"Name":"Kushagra", "Language":"Python", "Marks":{"A":45, "B":48, "C": 50}}
print(d)
print(d["Marks"])
print(d["Marks"]["A"])

# edit
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
print(d)
d[3] = "Crow"
print(d)

# Add new key value pair
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
d[6] = "Fast"
print(d)

# delete
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
del d

d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
del d[3]
print(d)

d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
d.clear()
print(d)

# operations
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}

for i in d:
    print(i, d[i])

# membership -> for keys
print(1 in d)

# functions
d = {1:"Apple", 2:"Ball", 3:"Cat", 4:"Dog", 5:"Elephant"}
print(len(d))
print(min(d))
print(max(d))
print(sum(d))
print(sorted(d))
print(sorted(d, reverse=True))
print(d.keys())
print(d.values())