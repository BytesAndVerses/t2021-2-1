# t2021-2-1
TANDEMLOOP_ASSESSMENT

## Programming Language Used:
Python

## Problem Descriptions:
### Problem-1: Solution for Problem-1
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

### Problem-2:Solution for Problem-2
  def generate_series(a):
    # Generate the series
    series = []
    for i in range(a):
        series.append(2 * i + 1)  # Formula for odd numbers
    return series

# Input from the user
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        # Call the function and display the result
        result = generate_series(a)
        print("Output:", ', '.join(map(str, result)))
except ValueError:
    print("Error: Please enter a valid integer.")

### Problem-3: Solution for Problem-3
  def generate_series(a):
    if a % 2 == 0:  # Check if the number is even
        a -= 1  # Use (a-1) for even inputs
    
    # Generate the series
    series = [2 * i + 1 for i in range(a)]  # Generate first `a` odd numbers
    return series

# Input from the user
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        # Generate and print the series
        result = generate_series(a)
        print("Output:", ', '.join(map(str, result)))
except ValueError:
    print("Error: Please enter a valid integer.")

### Problem-4: Solution for Problem-4
  def count_multiples(numbers):
    # Initialize a dictionary to store counts for numbers 1 to 9
    result = {i: 0 for i in range(1, 10)}
    
    # Loop through each number in the input list
    for num in numbers:
        # Check divisibility for each number from 1 to 9
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1

    return result

# Input list
input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Get the result
output = count_multiples(input_numbers)

# Print the output
print(output)


#### Instructions Followed:
- Created separate files for each problem.
- Solutions are written in Python with proper comments explaining the logic.
