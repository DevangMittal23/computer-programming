# Function to Calculate GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))