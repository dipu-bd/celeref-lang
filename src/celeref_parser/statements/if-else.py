import logging

from . import Statement

logger = logging.getLogger(__name__)


class IfElse(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        if self.variables["state"]:
            self.variables['state'] = self.__eval(self.source[0])
        elif len(self.source) == 2:
            self.variables['state'] = self.__eval(self.source[1])
