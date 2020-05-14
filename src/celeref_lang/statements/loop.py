import logging

from . import Statement

logger = logging.getLogger(__name__)


class Loop(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        # logger.debug('source: %s', self.source)
        output = []
        for item in self._get_list():
            self.variables['state'] = item
            super()._eval(self.source)
            output.append(self.result)
        self.variables['state'] = output
        # logger.debug('variables: %s', self.variables)

    def _get_list(self):
        if hasattr(self, '_list'):
            return self._list
        state = self.variables['state']
        if isinstance(state, list):
            self._list = state
        elif isinstance(state, int):
            self._list = range(0, state, -1 if state < 0 else 1)
        elif isinstance(state, str):
            self._list = list(state)
        elif isinstance(state, dict):
            self._list = state.items()
        else:
            self._list = []
        return self._list
