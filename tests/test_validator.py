import pytest
from configlib.validator import validate_config, ConfigValidationError

valid_config = {"host": "localhost", "port": 8080}
valid_schema = {
    "type": "object",
    "properties": {
        "host": {"type": "string"},
        "port": {"type": "integer"}
    },
    "required": ["host", "port"]
}

def test_valid_config():
    validate_config(valid_config, valid_schema)

def test_invalid_config_missing_key():
    invalid = {"host": "localhost"}
    with pytest.raises(ConfigValidationError):
        validate_config(invalid, valid_schema)

def test_invalid_config_type():
    invalid = {"host": "localhost", "port": "not a number"}
    with pytest.raises(ConfigValidationError):
        validate_config(invalid, valid_schema)
