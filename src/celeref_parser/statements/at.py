import logging

from . import Statement

logger = logging.getLogger(__name__)


class At(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        try:
            state = self.variables['state']
            self.variables['state'] = state[self.source]
        except IndexError:
            self.variables['state'] = None
        except TypeError:
            self.variables['state'] = None
        except KeyError:
            self.variables['state'] = None
        logger.debug(self.variables)
