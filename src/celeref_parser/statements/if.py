import logging

from . import Statement

logger = logging.getLogger(__name__)


class If(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        if self.variables["state"]:
            statement = Statement({'block':  self.source}, variables=self.variables)
            statement.execute()
            self.variables.update(statement.variables)
        logger.debug(self.variables)
