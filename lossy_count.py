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

def lossy_count(file, k):
    # Read the preprocessed text file
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # Estimate the k most frequent letters, running Lossy-Count algorithm
    return lossy_count(text, k)

# Parse the command line arguments
#parser = argparse.ArgumentParser()
#parser.add_argument("--input", "-i", help="Path to the input text file", required=True)
#args = parser.parse_args()
#
## Read the preprocessed text file
#with open(args.input, "r", encoding="utf-8") as f:
#    text = f.read()
#
## Estimate the k most frequent letters, running Lossy-Count algorithm for k = 3, k = 5 and k = 10.
#for k in [3, 5, 10]:
#    print(f"Top {k} letters:")
#    for letter, count in lossy_count(text, k).items():
#        print(f"{letter}: {count}")
#    print()