# UC6 – Return the GCD Value from Function

def calculate_gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_gcd(num1, num2)

print("GCD of", num1, "and", num2, "is:", result)