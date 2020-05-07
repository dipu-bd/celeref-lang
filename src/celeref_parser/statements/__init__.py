import importlib
import logging
import os
import re
from typing import Any, Mapping

logger = logging.getLogger(__name__)


# This list will be auto-generated
all_statements = {}


class Statement:
    def __init__(self,
                 source: Mapping[str, Any],
                 variables: Mapping[str, Any] = {}):
        self.source: Mapping[str, Any] = source
        self.variables: dict = dict()
        self.variables.update(variables or {})
        self.variables.setdefault('state', None)

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


# Auto-import all submodules in the current directory
__module_regex = re.compile(r'^([^_.][^.]+).py[c]?$', re.IGNORECASE)
for entry in os.listdir(__path__[0]):
    file_path = os.path.join(__path__[0], entry)
    if not os.path.isfile(file_path):
        continue
    regex_result = __module_regex.findall(entry)
    if len(regex_result) != 1:
        continue
    module_name = regex_result[0]
    module = importlib.import_module('.' + module_name, package=__package__)
    for key in dir(module):
        item = getattr(module, key)
        if type(item) == type(Statement) and item.__base__ == Statement:
            all_statements[module_name] = item
