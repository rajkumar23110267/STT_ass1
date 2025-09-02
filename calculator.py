"""
A simple calculator module with basic arithmetic operations.
"""

class Calculator:
    """A class that performs basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the division of two numbers. Raises ZeroDivisionError if b is 0."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))


if __name__ == "__main__":
    main()
