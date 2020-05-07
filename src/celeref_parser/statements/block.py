import logging

from . import Statement

logger = logging.getLogger(__name__)


class Block(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        for item in self.source:
            statement = Statement(item, variables=self.variables)
            statement.execute()
            self.variables.update(statement.variables)
        logger.debug(self.variables)
