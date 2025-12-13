import sys

print("starting")

#"sys.exit()"
print("ending")

import sys

print(sys.path)

import sys

print(sys.version)

import platform

print(platform.system())
print(platform.release())
print(platform.processor())

import random

random.seed(10) # Same Output after Excecution
print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 10))

names = ['krishna', 'nithin', 'sumanth', 'santosh', 'harsha', 'Prasad', 'Ajay']
print(random.choice(names))
print(random.choices(names, k = 3))
print("Before: ", names)
random.shuffle(names)
print("after: ", names)
