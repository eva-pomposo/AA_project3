from collections import defaultdict
import argparse

def lossy_count(text, k):
    # Create a defaultdict to store the letter counts
    letter_counts = defaultdict(int)

    # Iterate through each letter in the text and increment the count for that letter, ignore whitespace
    for letter in text:
        if letter.isspace():
            continue
        letter_counts[letter] += 1
        # If the number of items in the dictionary exceeds the maximum value, k, remove the item with the lowest count
        if len(letter_counts) > k:
            min_item = min(letter_counts, key=letter_counts.get)
            del letter_counts[min_item]

    # Sort the letters by their estimated count in descending order
    return dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", help="Path to the input text file", required=True)
args = parser.parse_args()

# Read the preprocessed text file
with open(args.input, "r", encoding="utf-8") as f:
    text = f.read()

# Estimate the most frequent letters using the Lossy-Count algorithm with k = 10
frequent_letters = lossy_count(text, 10)

# Print the estimated counts of the most frequent letters
for letter, count in frequent_letters.items():
    print(f"{letter}: {count}")
