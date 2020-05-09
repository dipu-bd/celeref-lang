#!/usr/bin/env python3

import sys
import logging
from celeref_lang.main import main
from celeref_lang.statements import all_statements
from celeref_lang.functions import public_functions

logging.basicConfig(level=logging.DEBUG)

print(all_statements)
print()

main()
