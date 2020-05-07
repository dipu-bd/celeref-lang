#!/usr/bin/env python3

import sys
import logging
from celeref_parser import create_app
from celeref_parser.statements import all_statements

logging.basicConfig(level=logging.DEBUG)

print(all_statements)
print()

if len(sys.argv) < 2:
    print('Need a valid JSON file')
    exit(1)

app = create_app(sys.argv[1])
app.execute()

print()
print(app.result)
