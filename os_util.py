#!/usr/bin/env python3.8.0

import os
import glob
import shutil

try:
    os.mkdir('./processes')
except OSError:
    print("Directory called 'processes' ia already exists")

files = glob.glob('./new/receipt_[0-9].json')
for file in files:
    shutil.move(file, './processes/' + file[6:])
    print('Successfuly moved ' + file + ' to ./processes/' + file[6:])





"""
print(os.listdir('./new'))
for item in os.listdir('./new'):
    print(item)
print(type(os.listdir('./new')))
"""


"""
try:
    os.makedirs('dir')
except FileExistsError:
    print('The desired name is already exists.')
except:
    print('An error occured')
"""


"""
if not os.path.exists('sub-dir'):
    os.makedirs('sub-dir')
"""


"""
x = '3'
try:
    print(x + 5)
except NameError:
    print('x isn\'t defined')
except:
    print('A problem has occured')
"""
