#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1])
output_file = open(sys.argv[2], 'w')

input_lines = input_file.readlines()

events = {}
temp_event, event_id, header = '', '', ''

for line in input_lines:
    if 'BEGIN:VEVENT' in line:
        break
    else:
        header += line

for line in input_lines:
    if 'BEGIN:VEVENT' in line:
        temp_event = line
    elif 'DTSTART' in line:
        temp_event += line
        event_id = line  # Note: Overwrites any previous event with the same DTSTART
    elif 'END:VEVENT' in line:
        temp_event += line.rstrip()
        events[event_id] = temp_event
    else:
        temp_event += line

output_file.write(header[:-1])

for line in events.values():
    output_file.write(line)

output_file.write('END:VCALENDAR')
