import re
import string
import unicodedata

def process_text(text):
    # Remove Project Gutenberg file headers
    # the fisrt header start in the line 1 and ends with *** *** , with some text in between
    text = re.sub(r"^.*?\*\*\*.*?\*\*\*.*?\n", "", text, flags=re.DOTALL)
    # the second header ends in the last line and starts with *** *** , with some text in between
    text = re.sub(r"\*\*\*.*?\*\*\*.*?$", "", text, flags=re.DOTALL)
    
    # Remove all stop-words and punctuation marks
    stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
                  'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
                  'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                  'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
                  'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                  'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
                  'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
                  'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                  'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
                  'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
                  'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                  'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
    text = text.translate(str.maketrans("", "", string.punctuation)).replace("“", "").replace("”", "").replace("‘", "").replace("’", "").replace("„", "").replace("‚", "").replace("«", "").replace("»", "").replace("æ", "").replace("—", "")
    text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    text = re.sub(r"\d+", "", text) # remove numbers
    text = " ".join([word for word in text.split() if word.lower() not in stop_words])

    # Convert all letters to uppercase
    return text.upper()

def file_processor(input_file, output_file):
    # Read the text file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Process the text
    text = process_text(text)

    # Save the processed text to a output file
    with open(output_file, "w") as f:
        f.write(text)