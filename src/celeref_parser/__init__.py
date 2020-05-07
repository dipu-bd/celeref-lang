import json
import logging
from typing import Any, Mapping

from .statements import Statement
from .utils.validator import validate_schema

logger = logging.getLogger(__name__)


class Instance(Statement):
    def __init__(self, data: Mapping[str, Any]):
        validate_schema(data)
        super().__init__(data['app'])
        self.name = data.get('name', 'App')
        self.version = data.get('version', None)


def create_app(filename: str) -> Instance:
    with open(filename) as fp:
        data = json.load(fp)
        return Instance(data)
