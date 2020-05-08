import logging

from . import Statement

logger = logging.getLogger(__name__)


class SwitchBlock(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        for source in self.source:
            condition_source = source.get('condition')
            condition = self.__eval(condition_source)
            if condition:
                block_source = source.get('block', [])
                self.variables['state'] = self.__eval(block_source)
