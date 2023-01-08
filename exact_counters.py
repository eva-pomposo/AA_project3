from collections import defaultdict

def count_letters(text):
    # Create a defaultdict to store the letter counts
    letter_counts = defaultdict(int)

    # Iterate through each letter in the text and increment the count for that letter, ignore whitespace
    for letter in text:
        if letter.isspace():
            continue
        letter_counts[letter] += 1

    return dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    #return letter_counts

def exact_counters(preprocessed_file, result_file):
    # Read the preprocessed text file
    with open(preprocessed_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Count the occurrences of each letter
    exact_counts = count_letters(text)

    # Calculate the total number of bits required to store the exact counts
    total_bits = 0
    # Write results to file
    with open("results/exact_counts_" + result_file, "w") as f:
        f.write("letter order count\n")
        for i, (letter, count) in enumerate(exact_counts.items()):
            f.write(f"{letter} {i+1} {count} \n") 
            total_bits += count.bit_length()

    print(f"Total bits required to store exact counts: {total_bits}")
    print()

    return exact_counts