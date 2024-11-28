#Higher-Order Function: Function as Argument
def apply_function(func, x):
    return func(x)

double = lambda x: x * 2
print(apply_function(double, 5))
