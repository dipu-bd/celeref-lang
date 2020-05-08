import logging

from . import Statement

logger = logging.getLogger(__name__)


class MoveVariables(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        for new_var, old_var in self.source.items():
            self.variables[new_var] = self.variables.get(old_var, None)
        logger.debug('variables: %s', self.variables)
