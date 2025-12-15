def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))

def power(base, exp):
    if exp == 0:          # base case
        return 1
    else:
        return base * power(base, exp - 1)

b = 2
e = 3
print(b, "power", e, "is", power(b, e))