"""
JSON Schema validation utilities.

Loads Draft-07 JSON schema files from the ``schemas/`` directory and
validates response data against them using the ``jsonschema`` library.
"""

import json
import os
from typing import Any, Dict

import jsonschema
from jsonschema import ValidationError, validate

# Resolve the schemas directory relative to this module's location:
# this file lives in python_suite/utils/, so two levels up is python_suite/
_UTILS_DIR: str = os.path.dirname(os.path.abspath(__file__))
_SUITE_DIR: str = os.path.dirname(_UTILS_DIR)
SCHEMAS_DIR: str = os.path.join(_SUITE_DIR, "schemas")


def load_schema(schema_name: str) -> Dict[str, Any]:
    """
    Load and parse a JSON schema file from the schemas directory.

    Args:
        schema_name: Filename of the schema (e.g. ``"post_schema.json"``).

    Returns:
        The parsed schema as a Python dict.

    Raises:
        FileNotFoundError: If the schema file does not exist.
        json.JSONDecodeError: If the schema file contains invalid JSON.
    """
    schema_path = os.path.join(SCHEMAS_DIR, schema_name)
    if not os.path.exists(schema_path):
        raise FileNotFoundError(
            f"Schema file not found: {schema_path}\n"
            f"Expected schemas directory: {SCHEMAS_DIR}"
        )
    with open(schema_path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_schema(data: Any, schema_name: str) -> None:
    """
    Validate *data* against the named JSON Schema (Draft-07).

    Args:
        data: The value to validate — typically a parsed JSON response body.
        schema_name: Filename of the schema to validate against
            (e.g. ``"post_schema.json"``).

    Raises:
        jsonschema.ValidationError: If *data* does not conform to the schema.
        jsonschema.SchemaError: If the schema file itself is malformed.
        FileNotFoundError: If the schema file cannot be found.
    """
    schema = load_schema(schema_name)
    validate(instance=data, schema=schema)
