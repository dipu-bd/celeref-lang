import json
import logging
from typing import Any, Mapping

from jsonschema import ValidationError, validate
from requests import HTTPError

from .file_adapter import create_session

logger = logging.getLogger(__name__)


class SchemaError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def load_schema(url: str) -> Mapping[str, Any]:
    sess = create_session()
    resp = sess.get(url, allow_redirects=True)
    resp.raise_for_status()
    return json.loads(resp.text)


def validate_schema(data: Mapping[str, Any]) -> bool:
    try:
        schema = load_schema(data['$schema'])
        validate(instance=data, schema=schema)
    except ValidationError as err:
        raise SchemaError('Failed to validate JSON\n%s' % err.message)
    except HTTPError as err:
        raise SchemaError('Failed to fetch schema\n%s' % str(err))
    except json.JSONDecodeError as err:
        raise SchemaError('Failed to parse schema\n%s' % err.msg)
