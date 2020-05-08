import logging

from . import Statement

logger = logging.getLogger(__name__)


class SetVariables(Statement):
    def __init__(self, body, variables={}):
        super().__init__(body, variables=variables)

    def execute(self):
        self.variables.update(self.source)
