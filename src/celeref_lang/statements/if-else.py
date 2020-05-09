import logging

from . import Statement

logger = logging.getLogger(__name__)


class IfElse(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        if self.variables['state']:  # state is True
            super()._eval(self.source[0])
        elif len(self.source) > 1:   # has else block
            super()._eval(self.source[1])
        logger.debug('variables: %s', self.variables)
