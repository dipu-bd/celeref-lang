import logging

from . import Statement

logger = logging.getLogger(__name__)


class Dot(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        # logger.debug('source: %s', self.source)
        self.variables['state'] = getattr(self.variables['state'], self.source, None)
        # logger.debug('variables: %s', self.variables)
