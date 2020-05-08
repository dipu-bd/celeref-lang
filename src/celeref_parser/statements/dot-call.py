import logging

from .call import Call

logger = logging.getLogger(__name__)


class DotCall(Call):
    def __init__(self, source, variables={}):
        super().__init__(source, variables=variables)

    def execute(self):
        method_name = self.source.get('method', '')
        method = getattr(self.variables['state'], method_name)

        args = self._get_args()
        kwargs = self._get_kwargs()
        self.variables['state'] = method(*args, **kwargs)
