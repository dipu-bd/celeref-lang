import logging

from . import Statement

logger = logging.getLogger(__name__)


class SwitchBlock(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        for source in self.source:
            condition_source = source.get('condition')
            super()._eval(condition_source)
            if self.variables['state']:
                if 'true' in source:
                    super()._eval(source['true'])
            else:
                if 'false' in source:
                    super()._eval(source['false'])
            if 'finally' in source:
                super()._eval(source['finally'])
        logger.debug('variables: %s', self.variables)
