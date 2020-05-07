import logging

from . import Statement

logger = logging.getLogger(__name__)


class Set(Statement):
    def __init__(self, body, variables={}):
        super().__init__(body, variables=variables)

    def execute(self):
        logger.debug(self.source)
        self.variables.update(self.source)
        logger.debug(self.variables)
