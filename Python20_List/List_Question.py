# ========= List Questions =========

# Implement title function
sample = "hey i am kushagra"

print(sample.split())

l = []

for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())

print(l)
print(" ".join(l))


# extract abc from abc@gmail.com
sample = "abc@gmail.com"
print(sample[:sample.find('@')])

# remove duplicate element 
sample1 = [1, 1, 2, 2, 3, 3, 4, 4]
sample2 = [1, 1, 2, 2, 1, 3, 4, 4, 2]

l = []

for i in sample2:
    if i not in l:
        l.append(i)

print(l)
