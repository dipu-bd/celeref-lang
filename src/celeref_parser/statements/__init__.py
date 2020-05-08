import glob
import importlib
import logging
import os
from typing import Any, Callable, Mapping

logger = logging.getLogger(__name__)


# This lists will be auto-generated
all_statements = {}


class Statement:
    def __init__(self,
                 source: Mapping[str, Any],
                 variables: Mapping[str, Any] = {}):
        '''Initialize a new statement'''
        self.source: Mapping[str, Any] = source
        self.variables: dict = dict()
        self.variables.update(variables or {})
        self.variables.setdefault('state', None)
        self.methods: dict = dict()

    @property
    def result(self):
        '''Returns the current state'''
        return self.variables['state']

    def execute(self):
        '''Executes the script, and returns the last state'''
        result = self.__eval(self.source)
        self.variables['state'] = result
        return result

    def __eval(self, source: Mapping[str, Any]):
        '''Evaluates the source preserving the current state'''
        state = self.variables['state']
        try:
            if isinstance(source, dict):
                key, source = source.items()[0]
                builder: Statement = all_statements[key]
                statement = builder(source, self.variables)
                result = statement.execute()
                self.variables.update(statement.variables)
                return result
            elif isinstance(source, list):
                for source_block in source:
                    result = self.__eval(source_block)
                    self.variables['state'] = result
                return self.variables['state']
            else:
                return source
        finally:
            self.variables['state'] = state


# Auto-import all statements
_cur_dir_ = os.path.dirname(__file__)
for entry in glob.glob(_cur_dir_ + '/*.py'):
    module_name = '.'.join(os.path.basename(entry).split('.')[:-1])
    if module_name[0] in '_.':
        continue
    module = importlib.import_module('.' + module_name, package=__package__)
    for key in dir(module):
        item = getattr(module, key)
        if type(item) == type(Statement) and item.__base__ == Statement:
            all_statements[module_name] = item
