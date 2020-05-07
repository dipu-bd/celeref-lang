import logging

from . import Statement

logger = logging.getLogger(__name__)


class SaveState(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        self.variables[self.source] = self.variables['state']
        logger.debug(self.variables)
