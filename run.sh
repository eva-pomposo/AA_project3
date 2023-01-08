#!/bin/bash

# Run the main.py script for each of the literary works
python3 main.py -i literary_works/Romeo_and_Juliet_finnish.txt -o processed_files/Romeo_and_Juliet_finnish.txt -r Romeo_and_Juliet_finnish.txt -s stop-words/finnish.txt
python3 main.py -i literary_works/Romeo_and_Juliet_french.txt -o processed_files/Romeo_and_Juliet_french.txt -r Romeo_and_Juliet_french.txt -s stop-words/french.txt
python3 main.py -i literary_works/Romeo_and_Juliet_dutch.txt -o processed_files/Romeo_and_Juliet_dutch.txt -r Romeo_and_Juliet_dutch.txt -s stop-words/dutch.txt
python3 main.py -i literary_works/Romeo_and_Juliet_english.txt -o processed_files/Romeo_and_Juliet_english.txt -r Romeo_and_Juliet_english.txt -s stop-words/english.txt
python3 main.py -i literary_works/Romeo_and_Juliet_german.txt -o processed_files/Romeo_and_Juliet_german.txt -r Romeo_and_Juliet_german.txt -s stop-words/german.txt
python3 main.py -i literary_works/Nazareth.txt -o processed_files/Nazareth.txt -r Nazareth.txt -s stop-words/english.txt
python3 main.py -i literary_works/lusiadas.txt -o processed_files/lusiadas.txt -r lusiadas.txt -s stop-words/english.txt

# Run the graphics.py script
python3 graphics.py
