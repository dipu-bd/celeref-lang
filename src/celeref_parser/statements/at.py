import logging
from typing import Union

from . import Statement

logger = logging.getLogger(__name__)


class At(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        state = self.variables['state']
        index = self.__eval(self.source)
        try:
            if hasattr(state, '__getitem__'):
                self.variables['state'] = state[index]
            else:
                self.variables['state'] = None
        except Union[IndexError, TypeError, KeyError]:
            self.variables['state'] = None
