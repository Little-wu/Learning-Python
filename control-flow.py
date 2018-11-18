#!user/bin/env python
# using python3.6

# Boolean:True and False; error:true false

# define a variable
flag = True
# output True
print(flag)

# compare operator
#  == != < > <= >=
# output False
print('Hello' == 'hello')
# output False
print('12' == 12)

# Boolean operator
# and not or
# output False
print(False and True)
# output True
print(False or True)

# control flow
name = 'xiao'

if name == 'xiao':
    print(True)

if name == 'xiao':
    print(True)
else:
    print(False)

if name == 'li':
    print('li')
elif name == 'ming':
    print('ming')
elif name == 'sha':
    print('sha')
else:
    print('xiao')

# loop while for
i = 0

# output 1 2 3 4 6
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 7:
        break
    print(i)

# rang(begin number,end number, increase value)
# output 2 4 6 8 10 12 14 16 18
for num in range(2, 20, 2):
    print(num)

# import a module 
import random

# create a number between 1 and 10
print(random.randint(1, 10))
