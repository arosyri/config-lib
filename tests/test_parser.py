import pytest
from configlib import parser
import tempfile
import os

def test_load_yaml_config():
    yaml_content = "host: localhost\nport: 8080\n"
    with tempfile.NamedTemporaryFile(delete=False, suffix='.yaml') as tmp:
        tmp.write(yaml_content.encode('utf-8'))
        tmp_path = tmp.name

    result = parser.load_config(tmp_path)
    assert result == {'host': 'localhost', 'port': 8080}
    os.remove(tmp_path)

def test_load_json_config():
    json_content = '{"host": "localhost", "port": 8080}'
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        tmp.write(json_content.encode('utf-8'))
        tmp_path = tmp.name

    result = parser.load_config(tmp_path)
    assert result == {'host': 'localhost', 'port': 8080}
    os.remove(tmp_path)

def test_unsupported_format():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp:
        tmp.write(b"unsupported")
        tmp_path = tmp.name

    with pytest.raises(parser.ConfigParserError):
        parser.load_config(tmp_path)
    os.remove(tmp_path)
