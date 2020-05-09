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
                 source: Any,
                 variables: Mapping[str, Any] = {}):
        '''Initialize a new statement'''
        self.source: Any = source
        self.variables: dict = dict()
        self.variables.update(variables or {})
        self.variables.setdefault('state', None)

    @property
    def result(self):
        '''Returns the current state'''
        return self.variables['state']

    def execute(self) -> None:
        '''Executes the script, and returns the last state'''
        logger.debug('source: %s', self.source)
        self._eval(self.source)
        logger.debug('variables: %s', self.variables)

    def _eval(self, source: Any):
        if isinstance(source, list):
            for block in source:
                self._eval(block)
        elif isinstance(source, dict):
            if len(source) == 1:
                [(key, source)] = source.items()
                builder: Statement = all_statements[key]
                statement = builder(source, self.variables)
                statement.execute()
                self.variables.update(statement.variables)
        else:
            self.variables['state'] = source


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
