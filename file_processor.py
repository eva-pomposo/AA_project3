import re
import string
import unicodedata

def process_text(text, stopwords_file):
    # Remove Project Gutenberg file headers
    # the first header start in the line 1 and ends with *** *** , with some text in between
    text = re.sub(r"^.*?\*\*\*.*?\*\*\*.*?\n", "", text, flags=re.DOTALL)
    # the second header ends in the last line and starts with *** *** , with some text in between
    text = re.sub(r"\*\*\*.*?\*\*\*.*?$", "", text, flags=re.DOTALL)
    
    # Remove all stop-words and punctuation marks
    with open(stopwords_file, "r") as f:
        stop_words = f.read().splitlines()
    stop_words = set(stop_words)

    text = text.translate(str.maketrans("", "", string.punctuation)).replace("“", "").replace("”", "").replace("‘", "").replace("’", "").replace("„", "").replace("‚", "").replace("«", "").replace("»", "").replace("æ", "").replace("—", "").replace("Æ", "").replace("œ", "")
    text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    text = re.sub(r"\d+", "", text) # remove numbers
    text = " ".join([word for word in text.split() if word.lower() not in stop_words])

    # Convert all letters to uppercase
    return text.upper()

def file_processor(input_file, output_file, stopwords_file):
    # Read the text file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Process the text
    text = process_text(text, stopwords_file)

    # Save the processed text to a output file
    with open(output_file, "w") as f:
        f.write(text)