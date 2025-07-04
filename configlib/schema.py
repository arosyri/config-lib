import json
import os

class SchemaLoaderError(Exception):
    """Custom error for schema.py"""
    pass

def load_schema(filepath: str) -> dict:
    """Loads a JSON schema from a file"""
    if not os.path.exists(filepath):
        raise SchemaLoaderError(f"File {filepath} not found")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise SchemaLoaderError(f"The schema has a JSON error: {e}")
