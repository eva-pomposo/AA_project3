#!/bin/bash

# Run the main.py script for each of the literary works
python3 main.py -i literary_works/Romeo_and_Juliet_finnish.txt -o processed_files/Romeo_and_Juliet_finnish.txt -r Romeo_and_Juliet_finnish.txt
python3 main.py -i literary_works/Romeo_and_Juliet_french.txt -o processed_files/Romeo_and_Juliet_french.txt -r Romeo_and_Juliet_french.txt
python3 main.py -i literary_works/Romeo_and_Juliet_ducth.txt -o processed_files/Romeo_and_Juliet_ducth.txt -r Romeo_and_Juliet_ducth.txt
python3 main.py -i literary_works/Romeo_and_Juliet_english.txt -o processed_files/Romeo_and_Juliet_english.txt -r Romeo_and_Juliet_english.txt
python3 main.py -i literary_works/Romeo_and_Juliet_german.txt -o processed_files/Romeo_and_Juliet_german.txt -r Romeo_and_Juliet_german.txt
python3 main.py -i literary_works/Nazareth.txt -o processed_files/Nazareth.txt -r Nazareth.txt

# Run the graphics.py script
python3 graphics.py
