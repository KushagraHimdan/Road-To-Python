# ============== Break Continue Pass ===========

# break -> at a specific condition break the loop
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

print("")


# continue -> no code will run for perticular iteration
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")

print("")

# pass -> if logic is not sure then use it to pass the statement

for i in range(1, 11):
    pass