def add_fraction(fr1, fr2):
    numerator = (fr1[0] * fr2[1]) + (fr2[0] * fr1[1])
    denominator = fr1[1] * fr2[1]
    return (numerator, denominator)

def subtract_fraction(fr1, fr2):
    numerator = (fr1[0] * fr2[1]) - (fr2[0] * fr1[1])
    denominator = fr1[1] * fr2[1]
    return (numerator, denominator)

def multiply_fraction(fr1, fr2):
    numerator = fr1[0] * fr2[0]
    denominator = fr1[1] * fr2[1]
    return (numerator, denominator)

def divide_fraction(fr1, fr2):
    if fr2[0] == 0:
        return "Division by zero is not allowed"
    numerator = fr1[0] * fr2[1]
    denominator = fr1[1] * fr2[0]
    return (numerator, denominator)

def simplify_fraction(fr):
    common = gcd(fr[0], fr[1])
    return (fr[0] // common, fr[1] // common)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def menu():
    while True:
        num1 = float(input("Enter the numerator of the first fraction: "))
        num2 = float(input("Enter the denominator of the first fraction: "))
        if num2 == 0.0:
            print("Denominator cannot be zero!")
            continue
        num3 = float(input("Enter the numerator of the second fraction: "))
        num4 = float(input("Enter the denominator of the second fraction: "))
        if num4 == 0.0:
            print("Denominator cannot be zero!")
            continue
                
        print(f"So your fractions are: {num1}/{num2} and {num3}/{num4}, right? Enter 'yes' or 'no'")
        ans = input()
        if ans.lower() in ("yes", "y"):
            break
        else:
            print("Okay, let's try again.")

    fraction1 = (num1, num2)
    fraction2 = (num3, num4)
    
    print("What do you want to do?")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    option = int(input())
    
    if option == 1:
        result = simplify_fraction(add_fraction(fraction1, fraction2))
    elif option == 2:
        result = simplify_fraction(subtract_fraction(fraction1, fraction2))
    elif option == 3:
        result = simplify_fraction(multiply_fraction(fraction1, fraction2))
    elif option == 4:
        result = simplify_fraction(divide_fraction(fraction1, fraction2))
    else:
        print("Invalid input")
        return

    print(f"Result: {result[0]}/{result[1]}")

menu()
