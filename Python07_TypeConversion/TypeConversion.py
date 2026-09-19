# Pactice program -> add two numbers

num1 = input("First number : ") # 2
num2 = input("Second number : ") # 4
res = num1 + num2 # 2 + 4
print("Sum is : ", res)  # Sum is : 24 
print(type(num1)) # class -> str
print(type(num2)) # class -> str
print(type(res)) # class -> str
# Python takes input as a String 
# String is a universal format Other kinds of data type can also be stored in a string But reverse is not true


# type conversion

# implicit type conversion :  Type conversion automatically

res2 = 4 + 5.5
print(res2)
print(type(res2)) # float

res3 = 4 + 5+7j
print(res3)
print(type(res3)) # comlex

res4 = 4.7 + 5+7j
print(res4)
print(type(res4)) # comlex

# Explicit Type conversion Explicitly have to tell The Data type 
# Can only be done with compatible data types

res5 = int(4 + 5.5)
print(res5) # 9
print(type(res5)) # int

res6 = 4 + int("56")
print(res6) # 9
print(type(res6)) # int

res7 = str(6)
print(res7)
print(type(res7))

res8 = bool(1)
print(res8)
print(type(res8))

res9 = complex(6)
print(res9)
print(type(res9))

res10 = list("Kushagra")
print(res10)
print(type(res10))

# Type conversion Is not Permanent 
# Actual value don't change
res11 = 8.9
print(res11)
print(int(res11))


# now
first_num = int(input("First number : "))
second_num =  int(input("First number : "))
result = first_num +second_num
print("Sum is :", result)