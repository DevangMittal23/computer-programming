#Return Multiple Values from a Function
def arithmetic_operations(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = arithmetic_operations(10, 5)
print(add, sub, mul, div)
