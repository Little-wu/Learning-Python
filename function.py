#!user/bin/env python
# using python3.6

import random

# define a funcation
def printname(name):
    print('hello '+name)

printname('hahah')

# return number
def createnum():
    return random.randint(1, 10)

print(createnum())

# keyword 'global'
s1 = '123'
s2 = '456'
def spam():
    global s1
    s1 = '321'
    s2 = '654'
    print(s1, s2, sep=',')


spam()
# s1 change,s2 not change
print(s1, s2)

# exception
def div(dividBy):
    try:
        return 42/dividBy
    except ZeroDivisionError:
        print('Errot:Invalid argument.')

# output: 21.0
print(div(2))
# output: Errot:Invalid argument.
print(div(0))

