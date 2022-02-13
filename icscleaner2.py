#!/usr/bin/env python3

import sys

output_filename = 'out.ics'
input_file1 = open(sys.argv[1])
input_file2 = open(sys.argv[2])
output_file = open(output_filename, 'w')

input_lines1 = input_file1.readlines()

existing_events = 0

for line in input_lines1[0:len(input_lines1)]:
    output_file.write(line)
    if 'BEGIN:VEVENT' in line:
        existing_events += 1

print(f'{existing_events} existing events copied')
print('Adding events not already in input file ...')

input_lines2 = input_file2.readlines()

events = {}
temp_event, event_id = '', ''
already_exists = False
new_events = 0
duplicate_events = 0

for line in input_lines2:
    if 'BEGIN:VEVENT' in line:
        temp_event = line
        already_exists = False
    elif 'SUMMARY:' in line:  # TODO: Check if date is after first event of primary calendar instead
        if line in open(output_filename).readlines():
            already_exists = True
            duplicate_events += 1
    elif 'DTSTART' in line:
        temp_event += line
        event_id = line
    elif 'END:VEVENT' in line:
        if not already_exists:
            new_events += 1
            temp_event += line
            events[event_id] = temp_event
            # output_file.write(temp_event)
    else:
        temp_event += line

for line in events.values():
    output_file.write(line)

print(f'{new_events} events added, {duplicate_events} duplicates found')
print(f'Output file {output_filename} contains {existing_events + new_events} events')

output_file.write('END:VCALENDAR')
