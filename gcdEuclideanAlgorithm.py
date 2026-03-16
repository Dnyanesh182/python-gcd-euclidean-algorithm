# UC5 – Handle Case When Both Numbers are Equal

def calculate_gcd(a, b):

    if a == b:
        return a

    if a == 0:
        return b

    if b == 0:
        return a

    while b != 0:
        a, b = b, a % b

    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = calculate_gcd(num1, num2)

print("GCD is:", gcd)