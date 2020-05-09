import os
import re
import json
import logging
import requests
from typing import Any, Mapping

from jsonschema import validate

from .statements import Statement

logger = logging.getLogger(__name__)


class Instance(Statement):
    def __init__(self, data: Mapping[str, Any]):
        super().__init__(data['program'])
        self.name = data.get('name', 'program')
        self.version = data.get('version', None)


def read_json(filename: str) -> Mapping[str, Any]:
    data = {}
    with open(filename) as fp:
        data = json.load(fp)

    schema = {}
    try:
        url = data['$schema']
        if re.search(r'^https?://', url, flags=re.IGNORECASE):
            resp = requests.get(url, allow_redirects=True)
            resp.raise_for_status()
            schema = json.loads(resp.text)
        else:
            schema_path = os.path.join(filename, '..', url)
            with open(os.path.normpath(schema_path)) as fp:
                schema = json.load(fp)
    except Exception:
        logger.exception('Failed to get schema from %s', url)
        curdir = os.path.dirname(__file__)
        with open(os.path.join(curdir, 'schema', 'schema.json')) as fp:
            schema = json.load(fp)

    validate(instance=data, schema=schema)
    return data


def create_app(filename: str) -> Instance:
    return Instance(read_json(filename))
