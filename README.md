# Algoritmos Avançados 3rd Project — Most Frequent Letters

## Introduction

The goal is to identify the most frequent letters in text files using different methods, and to evaluate the quality of estimates regarding the exact counts.

In order to accomplish that, develop and test three different approaches:
* exact counters,
* approximate counters (Csurös’ counter),
* one algorithm to identify frequent items in data streams (Lossy-Count).

An analysis of the computational efficiency and limitations of the developed approaches has to be carried out.
For example, in terms of absolute and relative errors (lowest value, highest value, average value, etc.), average values, etc.
It can also be verified whether the same most frequent letters are identified, and in the same relative order.
And if the most frequent letters are similar in the text files of the same literary work in different languages.

For this you must:
* Compute the exact number of occurrences of each letter.
* Estimate the k most frequent letters, running your data stream algorithm for k = 3, k = 5 and k = 10.
* Perform a set of tests, repeating the approximate counts a few times.
* Compare the performance of the approximate counters and the data stream algorithm (for the different k values), between themselves and regarding the exact counts. c) Write a report (max. 8 pages).

## Data for the computational experiments – Simulating data streams

Obtain text files from literary works, in different languages – e.g., from the [Project Gutenberg](https://www.gutenberg.org/) 

Process the text files to:
* Remove the Project Gutenberg file headers.
* Remove all stop-words and punctuation marks.
* Convert all letters to uppercase.

## How to run

### Start by installing the requeriments, creating a virtual environment for that:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### CLI arguments 

To execute the main.py script (which runs the 3 algorithms developed for a given file) it is necessary to pass the following arguments:
```
--input: Path to the input text file
--output: Path to the output text file (preprocessed file)
--results: Name for the results files
--stopwords: Path to the stopwords file
```

Example of a command to run main.py:
```
python3 main.py -i literary_works/Nazareth.txt -o processed_files/Nazareth.txt -r Nazareth.txt -s stop-words/english.txt
```

## Author
Eva Bartolomeu, Nmec 98513