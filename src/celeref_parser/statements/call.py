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
        for source in self.source.get('args', []):
            args.append(super()._eval(source))
        return args

    def _get_kwargs(self):
        kwargs = {}
        for key, source in self.source.get('kwargs', {}):
            kwargs[key] = super()._eval(source)
        return kwargs
