# UC2 – Define a Function to Calculate GCD

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = calculate_gcd(num1, num2)

print("GCD of", num1, "and", num2, "is:", gcd)