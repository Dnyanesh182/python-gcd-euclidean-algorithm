# UC9 – Allow Multiple GCD Calculations Using Loop

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


while True:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 < 0 or num2 < 0:
        print("Error: Please enter non-negative integers only.")
        continue

    gcd = calculate_gcd(num1, num2)

    print(f"GCD of {num1} and {num2} is: {gcd}")

    choice = input("Do you want to calculate another GCD? (yes/no): ").lower()

    if choice != "yes":
        print("Program terminated.")
        break