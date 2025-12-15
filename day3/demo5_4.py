def multiply(a, b=2):
    return a * b

def calculate(operation, x, y=5):
    return operation(x, y)

print(calculate(multiply, x=4))
print(calculate(multiply, x=4, y=3))
