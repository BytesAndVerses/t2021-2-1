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
