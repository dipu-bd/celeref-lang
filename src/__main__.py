#!/usr/bin/env python3

import sys
import logging
from celeref_lang import create_app
from celeref_lang.statements import all_statements
from celeref_lang.functions import public_functions

# logging.basicConfig(level=logging.DEBUG)

# print(all_statements)
# print()

# print(public_functions)
# print()

if len(sys.argv) < 2:
    print('Need a valid JSON file')
    exit(1)

app = create_app(sys.argv[1])
app.execute()

# print()
# print(app.result)
