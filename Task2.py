def add(x, y):
    """Addition operation"""
    return x + y

def subtract(x, y):
    """Subtraction operation"""
    return x - y

def multiply(x, y):
    """Multiplication operation"""
    return x * y

def divide(x, y):
    """Division operation with error handling"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    """
    Main calculator function that:
    1. Prompts for two numbers
    2. Prompts for an operation
    3. Performs the calculation
    4. Displays the result
    """
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input operation
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        
        # Dictionary to map operations to functions
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }

        # Validate and perform calculation
        if operation in operations:
            try:
                result = operations[operation](num1, num2)
                print(f"\nResult: {num1} {operation} {num2} = {result}")
                return result
            except ValueError as e:
                print(f"Error: {e}")
                return None
        else:
            print("Invalid operation. Please choose +, -, *, or /.")

def main():
    """Main function to run the calculator"""
    while True:
        calculator()
        
        # Ask if user wants to continue
        continue_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()