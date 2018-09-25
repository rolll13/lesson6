file = open('regexp.py', 'r')
print(file.read())

file.seek(0)
lines = file.readlines()
print(lines)

file.close()

file = open('test_write1.txt', 'w')
file.write('Line1\nLine2\nLine3')
file.close()

file = open('regexp_copy.py', 'w')
file.writelines(lines)
file.close()

with open('test_write2', 'w') as file:
    file.write('Context manager')


import os
print('DIRS')
files = os.listdir('.')
for file in files:
    print(file, os.path.isdir(file))


def foo(a: int, b: str) -> int:
    a = [1, "str"]
    return a[0]


