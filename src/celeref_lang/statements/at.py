import logging
from typing import Union

from . import Statement

logger = logging.getLogger(__name__)


class At(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        state = self.variables['state']
        super()._eval(self.source)
        index = self.result
        try:
            if hasattr(state, '__getitem__'):
                self.variables['state'] = state[index]
            else:
                self.variables['state'] = None
        except Union[IndexError, TypeError, KeyError]:
            self.variables['state'] = None
        logger.debug('variables: %s', self.variables)
