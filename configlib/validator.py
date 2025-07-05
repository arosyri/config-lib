import jsonschema
from jsonschema.exceptions import ValidationError

class ConfigValidationError(Exception):
    """Custom error for incorrect configuration"""
    pass

def validate_config(config: dict, schema: dict) -> None:
    """
    Checks whether config matches the schema.
    If not, throws ConfigValidationError.
    """
    try:
        jsonschema.validate(instance=config, schema=schema)
    except ValidationError as e:
        raise ConfigValidationError(f"Validation error: {e.message}")
