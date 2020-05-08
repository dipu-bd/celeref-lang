import logging

from . import Statement

logger = logging.getLogger(__name__)


class LoadVariableToState(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        self.variables['state'] = self.variables[self.source]
        logger.debug('variables: %s', self.variables)
