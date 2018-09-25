def foo(a=1, b=2, c=3):
    return a, b, c

# print(foo)

def decorator(foo):
    def inner_function(*args, **kwargs):
        return foo(*args, **kwargs)
    return inner_function

foo = decorator(foo)


@decorator
def foo1():
    pass


# print(foo)
# print('!'*10)
# print(foo())


def function(a, b, c=1):
    return a, b, c


def decorator_with_params(p1, p2):
    print('decorator')
    def inner(func):
        print('inner')
        def inner1(*args, **kwargs):
            print('inner1')
            return func(*args, **kwargs)
        return inner1

    return inner

print(function)
print(decorator_with_params('1', '2'))
print(decorator_with_params('1', '2')(function))  # декорирование
print(decorator_with_params('1', '2')(function)(1, 2, 3))  # вызов


@decorator_with_params('1', '2')
def foo123(a=1, b=2):
    return













