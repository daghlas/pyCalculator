# Calculator App
# addition
def add(x, y):
    return x + y


# subtraction
def subtract(x, y):
    return x - y


# multiplication
def multiply(x, y):
    return x * y


# division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


print("Welcome to Calculator App!")
# arithmetic selection
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    # exit app
    if choice == '5':
        print("Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    # arithmetic workout & result display
    if choice == '1':
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        # error message
        print("Invalid input. Please try again.")
