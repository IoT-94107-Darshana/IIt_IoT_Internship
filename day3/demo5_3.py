def add(a, b):
    return a + b


def operate(func, x, y):
    return func(x, y)


result = operate(add, 10, 5)
print("Result:", result)
