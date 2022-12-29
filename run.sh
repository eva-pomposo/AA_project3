#!/bin/bash

# Run the preprocessing script
python3 file_processor.py -i literary_works/pg69644.txt -o processed_files/pg69644.txt 
# Run the exact and approximate counter scripts
python3 exact_counters.py -i processed_files/pg69644.txt  
python3 approximate_counters.py -i processed_files/pg69644.txt
