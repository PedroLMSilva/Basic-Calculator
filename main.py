# Program make a simple calculator that can add, subtract, multiply and divide using functions
import math


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function gives the percentage
def percentage(x, y):
    if x > 0 or y > 0:
        return str((x / y) * 100) + "%"
    else:
        return "Error - Negative numbers"


# This function gives the factorial of a number
def factorial(x):
    result = 1

    for i in range(1, x + 1):
        result = result * i

    return result


# This function gives the exponential of a number
def exponential(x, y):
    return x ** y


# This function gives the square root of a number
def squareroot(x):
    return math.sqrt(x)


# This function gives the logarithm of a number
def log(x):
    return math.log(x, 10)


def numinput():
    while True:
        try:
            number = float(input("Enter a number: "))
            break
        except ValueError:
            print("Not a number. Try again.")
    return number


def validadeinput():
    while True:
        try:
            inputChoice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
            break
        except ValueError:
            print("Not a number. Try again.")
    return inputChoice


def printmenu():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Percentage")
    print("6.Factorial")
    print("7.Exponential")
    print("8.Square Root")
    print("9.Logarithm")
    print("10.Exit")


printmenu()
while True:
    # take input from the user
    choice = validadeinput()

    # check if choice is one of the ten options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        if choice == '1':
            num1 = numinput()
            num2 = numinput()
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            num1 = numinput()
            num2 = numinput()
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = numinput()
            num2 = numinput()
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = numinput()
            num2 = numinput()
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            num1 = numinput()
            num2 = numinput()
            print(num1, "%", "of", num2, "=", percentage(num1, num2))

        elif choice == '6':
            num = numinput()
            print("Factorial of", num, "=", factorial(int(num)))

        elif choice == '7':
            num1 = numinput()
            num2 = numinput()
            print(num1, "^", num2, "=", exponential(num1, num2))

        elif choice == '8':
            num = numinput()
            print("Square root of", num, "=", squareroot(int(num)))

        elif choice == '9':
            num = numinput()
            print("Logarithm of", num, "=", log(int(num)))

        elif choice == '10':
            break

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            printmenu()
    else:
        print("Invalid Input")
