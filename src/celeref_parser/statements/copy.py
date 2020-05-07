import logging

from . import Statement

logger = logging.getLogger(__name__)


class Copy(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        for new_var, old_var in self.source.items():
            self.variables[new_var] = self.variables.get(old_var, None)
        logger.debug(self.variables)
