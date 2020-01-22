#!/usr/bin/env python3.8.0

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type = str, help = 'Enter the desired file to display in reverse order.') 
parser.add_argument('--limit', '-l', type = int, help = 'Enter the number of lines to read')

args = parser.parse_args()
"""
# I've done it with a bit help of Lidor's pdf.
with open(args.file, 'r') as f:
    lines = f.readlines()
    if args.limit:
        lines = lines[:args.limit]
    for line in lines:
        print(line.rstrip()[::-1])
"""

# I've done it woth no help.
i = 0
with open(args.file, 'r') as f:
    for line in reversed(list(f.readlines())):
        print(line.rstrip()[::-1])
        i += 1
        if i == args.limit:
            break

