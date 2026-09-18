# ============ Built in Module ================

# Module can be considered as a code library

# A file containing a set of function you want to include in your application

# Example of Python modules : 
# math 
# random 
# OS 
# time

# help("modules")

# math
import math

print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.ceil(5.8))
print(math.floor(5.34))

# random
import random

print(random.randint(1, 100))
a = [1, 3, 5, 7, 9]
random.shuffle(a)
print(a)

# time
import time

print(time.time())
print(time.ctime())

print("hello")
time.sleep(1)
print("world")

# OS
import os

print(os.getcwd())
print(os.listdir())