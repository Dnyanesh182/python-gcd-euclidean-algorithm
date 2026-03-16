# UC10 – Optimize Function Using Recursive Approach

def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a % b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = calculate_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd}")