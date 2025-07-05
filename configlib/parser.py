import json
import yaml
import os

class ConfigParserError(Exception):
    """Custom error for parser.py"""
    pass

def load_config(filepath: str) -> dict:
    """Loads a configuration file in YAML or JSON format"""
    if not os.path.exists(filepath):
        raise ConfigParserError(f"File {filepath} does not exist")

    _, ext = os.path.splitext(filepath)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            if ext in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif ext == '.json':
                return json.load(f)
            else:
                raise ConfigParserError(f"Unsupported file format: {ext}")
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ConfigParserError(f"Syntax error in {filepath}: {e}")
