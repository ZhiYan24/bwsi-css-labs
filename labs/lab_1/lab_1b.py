"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and prompts for an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the operation, result.

    Args:
        operation (str): The operation performed ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        result (float): The output of the calculation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def get_num(ordinal: str):
    while True:
        try:
            return float(input(f"Enter the {ordinal} number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = get_num("first")
    num2 = get_num("second")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
