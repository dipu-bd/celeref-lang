import logging

from .call import Call

logger = logging.getLogger(__name__)


class DotCall(Call):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        logger.debug('source: %s', self.source)
        method_name = self.source.get('method', '')
        method = getattr(self.variables['state'], method_name)

        args = super()._get_args()
        kwargs = super()._get_kwargs()
        self.variables['state'] = method(*args, **kwargs)
        logger.debug('variables: %s', self.variables)
