import logging

from . import Statement

logger = logging.getLogger(__name__)


class SwitchBlock(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        for case in self.source:
            condition_source = case.get('condition')
            super()._eval(condition_source)
            if self.variables['state']:
                if 'true' in case:
                    super()._eval(case['true'])
            else:
                if 'false' in case:
                    super()._eval(case['false'])
            if 'finally' in case:
                super()._eval(case['finally'])
        logger.debug('variables: %s', self.variables)
