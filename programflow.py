#!/usr/bin/env python3.8.0
"""
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))
"""

"""
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
"""

"""
tree1 = "ABC"
tree2 = "ABC"

if tree1 == tree2:
    print("The names of the trees are the same.")
else:
    print("The names of the trees aren't the same.")

x = dict(a=1, b=2)
print(x)
y = x.keys()
print(y)
print(type(y))

print(f"aaaa")

first = ""
last = ""
if first or last:
    print("One of them")
"""

"""
user = {'admin': True, 'active': False, 'name': 'Kevin'}
if user.get('admin') and user.get('active'):
    print('ACTIVE - (ADMIN) ' + user.get('name'))
elif user.get('admin'):
    print('(ADMIN) ' + user.get('name'))
elif user.get('active'):
    print('ACTIVE ' + user.get('name'))
"""


users = [
    {'admin': True, 'active': True, 'name': 'Kevin'},
    {'admin': True, 'active': False, 'name': 'Elisabeth'},
    {'admin': False, 'active': True, 'name': 'Josh'},
    {'admin': False, 'active': False, 'name': 'Kim'},
]

for user in users:
    if user.get('admin') and user.get('active'):
        print('ACTIVE - (ADMIN) ' + user.get('name'))
    elif user.get('admin'):
        print('(ADMIN) ' + user.get('name'))
    elif user.get('active'):
        print('ACTIVE ' + user.get('name'))
    else:
        print(user.get('name'))

for user in users:
    if user['admin'] and user['active']:
        prefix = 'ACTIVE - (ADMIN) '
    elif user['admin']:
        prefix = '(ADMIN) '
    elif user['active']:
        prefix = 'ACTIVE '
    else:
        prefix = ''
    print(prefix + user['name'])
