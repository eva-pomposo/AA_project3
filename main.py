import numpy as np
import argparse
import string
from csuros_counter import csuros_counter
from exact_counters import exact_counters
from file_processor import file_processor
from lossy_count import lossy_count

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", help="Path to the input text file", required=True)
parser.add_argument("--output", "-o", help="Path to the output text file (preprocessed file)", required=True)
parser.add_argument("--results", "-r", help="Name for the results files", required=True)
args = parser.parse_args()

text = file_processor(args.input, args.output)

# Count the occurrences of each letter
exact_counts = exact_counters(args.output, args.results)

# Initialize lists to store the absolute and relative errors for each test
absolute_errors_csuros_counter = []
relative_errors_csuros_counter = []
avg_frequent_letters_csuros_counter = {letter: 0 for letter in string.ascii_uppercase}

# Perform a set of tests and calculate metrics
for i in range(10):
    # Estimate the most frequent letters using the approximate floating-point counter with m = 100
    estimated_counts = csuros_counter(args.output)

    # Calculate the absolute errors, relative errors and average counts of each letter 
    for letter, exact_count in exact_counts.items():
        avg_frequent_letters_csuros_counter[letter] += estimated_counts[letter]
        estimated_count = estimated_counts[letter]
        absolute_error = abs(estimated_count - exact_count)
        relative_error = absolute_error / exact_count
        absolute_errors_csuros_counter.append(absolute_error)
        relative_errors_csuros_counter.append(relative_error)

# Divide the counts by the number of tests to get the average
for letter in avg_frequent_letters_csuros_counter:
    avg_frequent_letters_csuros_counter[letter] /= 10
avg_frequent_letters_csuros_counter = dict(sorted(avg_frequent_letters_csuros_counter.items(), key=lambda item: item[1], reverse=True))

# Compute the average, minimum, and maximum values for the absolute and relative errors
average_absolute_error = np.mean(absolute_errors_csuros_counter)
minimum_absolute_error = np.min(absolute_errors_csuros_counter)
maximum_absolute_error = np.max(absolute_errors_csuros_counter)
average_relative_error = np.mean(relative_errors_csuros_counter)
minimum_relative_error = np.min(relative_errors_csuros_counter)
maximum_relative_error = np.max(relative_errors_csuros_counter)

# Print the results for the Csuros counter
print("Error metrics for the Csuros counter:")
print(f"Average absolute error: {average_absolute_error:.2f}")
print(f"Minimum absolute error: {minimum_absolute_error:.2f}")
print(f"Maximum absolute error: {maximum_absolute_error:.2f}")
print(f"Average relative error: {average_relative_error:.2f}")
print(f"Minimum relative error: {minimum_relative_error:.2f}")
print(f"Maximum relative error: {maximum_relative_error:.2f}")
print()

# Write the average counts of the Csuros counter to a file
with open("results/csuros_counter_" + args.results, "w") as f:
    f.write("letter order count\n")
    for i, (letter, count) in enumerate(avg_frequent_letters_csuros_counter.items()):
        f.write(f"{letter} {i+1} {count} \n") 

# Estimate the k most frequent letters, running Lossy-Count algorithm for k = 3, k = 5 and k = 10, and write the results to a file
with open("results/lossy_count_" + args.results, "w") as f:
    f.write("letter k order count\n")
    for k in [3, 5, 10]:
        for i, (letter, count) in enumerate(lossy_count(args.output, k).items()):
            f.write(f"{letter} {k} {i+1} {count} \n")   
            # Calculate the absolute errors, relative errors and average counts of each letter
            exact_count = exact_counts[letter]
            absolute_error = abs(count - exact_count)
            relative_error = absolute_error / exact_count 
