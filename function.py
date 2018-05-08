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
