file = open('read_files.txt')
print(file.read())

f = open('E:/basicPython/file_handling/file/files/new/welcome.txt')
# print('-'*10,'directory')
# print(f.read())
print('-'*10,'readline')
print(f.readline()) # first line print korbe
f.close()

print('-'*10, 'with open')
# another system to open()
with open('read_files.txt') as n:
    print(n.read())


# create new file : 
try:
    c = open('demo.txt', 'x')
except Exception:
    print('already exists')
else:
    print('created success') # try succes hole
finally:
    print('it will works') # all time execute

import os
if os.path.exists('demo.txt'):
    os.remove('demo.txt')

