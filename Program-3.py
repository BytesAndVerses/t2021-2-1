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
