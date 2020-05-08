import logging

from ..functions import public_functions
from . import Statement

logger = logging.getLogger(__name__)


class Call(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        args = self.source['args']
        kwargs = self.source['kwargs']
        state = self.variables['state']
        method = public_functions.get(self.source, None)
        if not method:
            raise TypeError('No such method')
        self.variables['state'] = method(*args, **kwargs)
        logger.debug(self.variables)
