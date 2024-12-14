class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Convert to lowercase for consistency

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operation. Please choose addition, subtraction, multiplication, or division."

# Input values from the user
try:
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (addition, subtraction, multiplication, division): ")

    # Create a Calculator instance and perform the calculation
    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers for a and b.")
