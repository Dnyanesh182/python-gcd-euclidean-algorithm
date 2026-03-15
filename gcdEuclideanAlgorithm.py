# UC3 – Implement Euclidean Algorithm Logic

def calculate_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_gcd(num1, num2)

print("GCD is:", result)