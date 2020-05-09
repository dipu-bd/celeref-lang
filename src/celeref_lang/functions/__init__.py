import glob
import importlib
import logging
import os
from typing import Callable, Mapping

logger = logging.getLogger(__name__)


# This lists will be auto-generated
public_functions: Mapping[str, Callable] = {}


# Auto-import all public functions
_cur_dir_ = os.path.dirname(__file__)
for entry in glob.glob(_cur_dir_ + '/*.py'):
    module_name = '.'.join(os.path.basename(entry).split('.')[:-1])
    if module_name[0] in '_.':
        continue
    module = importlib.import_module('.' + module_name, package=__package__)
    for key in dir(module):
        if key[0] in '_.':
            continue
        item = getattr(module, key)
        if callable(item):
            function_name = module_name + '.' + key
            public_functions[function_name] = item


# Add safe built-in functions
public_functions['abs'] = abs
public_functions['all'] = all
public_functions['any'] = any
public_functions['ascii'] = ascii
public_functions['bin'] = bin
public_functions['bool'] = bool
public_functions['bytearray'] = bytearray
public_functions['bytes'] = bytes
public_functions['chr'] = chr
public_functions['divmod'] = divmod
public_functions['enumerate'] = enumerate
public_functions['float'] = float
public_functions['format'] = format
public_functions['hash'] = hash
public_functions['hex'] = hex
public_functions['input'] = input
public_functions['int'] = int
public_functions['iter'] = iter
public_functions['len'] = len
public_functions['list'] = list
public_functions['map'] = map
public_functions['max'] = max
public_functions['min'] = min
public_functions['next'] = next
public_functions['oct'] = oct
public_functions['ord'] = ord
public_functions['pow'] = pow
public_functions['print'] = print
public_functions['range'] = range
public_functions['reversed'] = reversed
public_functions['round'] = round
public_functions['set'] = set
public_functions['slice'] = slice
public_functions['sorted'] = sorted
public_functions['str'] = str
public_functions['sum'] = sum
public_functions['tuple'] = tuple
public_functions['type'] = type
public_functions['zip'] = zip
