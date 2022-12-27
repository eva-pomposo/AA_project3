from collections import defaultdict
import argparse

def count_letters(text):
    # Create a defaultdict to store the letter counts
    letter_counts = defaultdict(int)

    # Iterate through each letter in the text and increment the count for that letter, ignore whitespace
    for letter in text:
        if letter.isspace():
            continue
        letter_counts[letter] += 1
    return letter_counts

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", help="Path to the input text file", required=True)
args = parser.parse_args()

# Read the preprocessed text file
with open(args.input, "r", encoding="utf-8") as f:
    text = f.read()

# Count the occurrences of each letter
letter_counts = count_letters(text)

# Print the letter counts
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
