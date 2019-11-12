#!/usr/bin/env python
# Parse output from YCSB and output start- and end-timestamp

import sys
import re

if len(sys.argv) <= 1:
    print("Please enter input file name.")
    exit()

rfile = sys.argv[1]

# Read file and create list of lines
file = open(rfile, "r")
lines = list(map(lambda line: line.rstrip('\n'), file.readlines()))

# Remove everything before "Starting test"
def get_line_with_find(lines, regex):
    for index, line in enumerate(lines):
        if line.find('Starting test') != -1:
            return index
    return -1
        
body_index = get_line_with_find(lines, 'Starting test.')

body = lines[body_index + 1:]

# Get only data lines
regex_pattern = re.compile("^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]:[0-9]{3}")
data_lines = list(filter(lambda line: regex_pattern.match(line), body))

# Get first and last line
first_line = data_lines[0]
last_line = data_lines[-1]

# Parse the timestamps
start_time_string = first_line.split()[0] + ' ' + first_line.split()[1][:8]
end_time_string = last_line.split()[0] + ' ' + last_line.split()[1][:8]

# Print
print(start_time_string)
print(end_time_string)

