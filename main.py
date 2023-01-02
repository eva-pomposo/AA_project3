import numpy as np
import argparse
import string
from csuros_counter import csuros_counter
from exact_counters import exact_counters
from file_processor import file_processor

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", help="Path to the input text file", required=True)
parser.add_argument("--output", "-o", help="Path to the output text file", required=True)
args = parser.parse_args()

text = file_processor(args.input, args.output)

# Count the occurrences of each letter
exact_counts = exact_counters(args.output)

# Initialize lists to store the absolute and relative errors for each test
absolute_errors = []
relative_errors = []
avg_frequent_letters = {letter: 0 for letter in string.ascii_uppercase}

# Perform a set of tests and calculate metrics
for i in range(10):
    # Estimate the most frequent letters using the approximate floating-point counter with m = 100
    estimated_counts = csuros_counter(args.output)

    # Calculate the absolute errors, relative errors and average counts of each letter 
    for letter, exact_count in exact_counts.items():
        avg_frequent_letters[letter] += estimated_counts[letter]
        estimated_count = estimated_counts[letter]
        absolute_error = abs(estimated_count - exact_count)
        relative_error = absolute_error / exact_count
        absolute_errors.append(absolute_error)
        relative_errors.append(relative_error)

# Divide the counts by the number of tests to get the average
for letter in avg_frequent_letters:
    avg_frequent_letters[letter] /= 10
avg_frequent_letters = dict(sorted(avg_frequent_letters.items(), key=lambda item: item[1], reverse=True))

# Compute the average, minimum, and maximum values for the absolute and relative errors
average_absolute_error = np.mean(absolute_errors)
minimum_absolute_error = np.min(absolute_errors)
maximum_absolute_error = np.max(absolute_errors)
average_relative_error = np.mean(relative_errors)
minimum_relative_error = np.min(relative_errors)
maximum_relative_error = np.max(relative_errors)

# Print the results
print(f"Average absolute error: {average_absolute_error:.2f}")
print(f"Minimum absolute error: {minimum_absolute_error:.2f}")
print(f"Maximum absolute error: {maximum_absolute_error:.2f}")
print(f"Average relative error: {average_relative_error:.2f}")
print(f"Minimum relative error: {minimum_relative_error:.2f}")
print(f"Maximum relative error: {maximum_relative_error:.2f}")

# Print the average counts of the most frequent letters
for letter, count in avg_frequent_letters.items():
    print(f"{letter}: {count}")
