# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """

    Perform arithmetic operation on two numbers based on operation type.

    Args:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): Type of operation: 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - float: Result of the arithmetic operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Error: Unsupported operation"

    # Testing the function locally (optional)
    if __name__ == "__master__":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
