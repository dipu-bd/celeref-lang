import logging

from ..functions import public_functions
from . import Statement

logger = logging.getLogger(__name__)


class Call(Statement):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        method_name = self.source.get('method', '')
        method = public_functions.get(method_name)
        if not method:
            raise NotImplementedError("No public method '%s' is defined" % method_name)

        args = self._get_args()
        kwargs = self._get_kwargs()
        self.variables['state'] = method(*args, **kwargs)
        logger.debug('variables: %s', self.variables)

    def _get_args(self):
        args = []
        state = self.variables['state']
        for source in self.source.get('args', []):
            super()._eval(source)
            args.append(self.result)
        self.variables['state'] = state
        logger.debug('args: %s', args)
        return args

    def _get_kwargs(self):
        kwargs = {}
        state = self.variables['state']
        for key, source in self.source.get('kwargs', {}):
            super()._eval(source)
            kwargs[key] = self.result
        self.variables['state'] = state
        logger.debug('kwargs: %s', kwargs)
        return kwargs
