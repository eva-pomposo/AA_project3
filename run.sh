#!/bin/bash

# Run the preprocessing script
python3 file_processor.py -i literary_works/pg69644.txt -o processed_files/pg69644.txt 
# Run the exact counter
python3 exact_counters.py -i processed_files/pg69644.txt  
# Run the approximate counter
python3 approximate_counters.py -i processed_files/pg69644.txt
# Run the lossy counter
python3 lossy_count.py -i processed_files/pg69644.txt
