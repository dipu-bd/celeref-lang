import logging

from . import Statement

logger = logging.getLogger(__name__)


class Call(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        raise NotImplementedError()
