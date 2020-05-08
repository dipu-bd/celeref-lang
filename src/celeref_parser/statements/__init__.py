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
        self.source: Mapping[str, Any] = source
        self.variables: dict = dict()
        self.variables.update(variables or {})
        self.variables.setdefault('state', None)
        self.methods: dict = dict()

    def execute(self):
        logger.debug(self.source)
        if len(self.source.keys()) != 1:
            return self.variables['state']
        key = list(self.source.keys())[0]
        if key not in all_statements:
            logger.error('%s is not yet implemented', key)
            return self.variables['state']
        builder: Statement = all_statements[key]
        statement = builder(self.source[key], self.variables)
        statement.execute()
        self.variables.update(statement.variables)
        logger.debug("%s: %s", __name__, self.variables)

    @property
    def result(self):
        return self.variables['state']


# Auto-import all statements
_cdir_ = os.path.dirname(__file__)
for entry in glob.glob(_cdir_ + '/*.py', recursive=True):
    module_name = '.'.join(os.path.basename(entry).split('.')[:-1])
    if module_name[0] in '_.':
        continue
    module = importlib.import_module('.' + module_name, package=__package__)
    for key in dir(module):
        item = getattr(module, key)
        if type(item) == type(Statement) and item.__base__ == Statement:
            all_statements[module_name] = item
