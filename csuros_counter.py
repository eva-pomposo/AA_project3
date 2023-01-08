import random
import string

M = 1000

def fp_increment(x):
    t = x // M
    while t > 0:
        if random.getrandbits(1) == 1:
            return x
        t -= 1
    return x + 1

def estimate_frequent_letters(text):
    # Create a dictionary to store the letter counts
    letter_counts = {letter: 0 for letter in string.ascii_uppercase}

    # Iterate through each letter in the text and increment the count using fp_increment
    for letter in text:
        if letter.isspace():
            continue
        letter_counts[letter] = fp_increment(letter_counts[letter])

    # Sort the letters by their estimated count in descending order
    return dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))

def csuros_counter(file):
    # Read the preprocessed text file
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # Estimate the most frequent letters using the approximate floating-point counter with m = 100
    return estimate_frequent_letters(text)