import logging

from . import Statement

logger = logging.getLogger(__name__)


class DotCall(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        args = self.source['args']
        kwargs = self.source['kwargs']
        state = self.variables['state']
        method = getattr(state, self.source, None)
        self.variables['state'] = method(*args, **kwargs)
        logger.debug(self.variables)
