import re

s = "   lorem ipsum dolor sit amet H"


# достать первое слово
compiled = re.compile(r'^\s*(\w+)')
print(compiled.findall(s))


# вернуть первые 2 символа в каждом слове
compiled = re.compile(r'\s+(\w{1,2})')
print(compiled.findall(s))

# Вернуть список доменов адреса электоронной почты
s = "email1@gmail.com, email2@mail.ru, email3@yahoo.ru"
compiled = re.compile(r'@(\w[\w\-_.]+.\w+)')
print(compiled.findall(s))

# Извлечь дату из строки 12-12-1993
s = "32-12-1994 asdasd zxczxc 11-08-2014"
compiled = re.compile('(([0-2][0-9]|3[0-1])-(0[0-9]|1[0-2])-\d{4})')
print(compiled.findall(s))
