# UC8 – Validate Input for Non-Negative Integers

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < 0 or num2 < 0:
    print("Error: Please enter non-negative integers only.")
else:
    gcd = calculate_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {gcd}")