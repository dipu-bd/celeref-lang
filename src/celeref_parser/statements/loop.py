import logging

from . import Statement

logger = logging.getLogger(__name__)


class Loop(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug(self.source)
        output = []
        for item in self._get_list():
            self.variables['state'] = item
            statement = Statement({'block':  self.source}, variables=self.variables)
            statement.execute()
            self.variables.update(statement.variables)
            output.append(self.variables['state'])
        self.variables['state'] = output
        logger.debug(self.variables)

    def _get_list(self):
        state = self.variables['state']
        if isinstance(state, list):
            return state
        elif isinstance(state, int):
            return range(0, state, -1 if state < 0 else 1)
        elif isinstance(state, str):
            return list(state)
        elif isinstance(state, dict):
            return state.items()
        else:
            return []
