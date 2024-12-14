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
