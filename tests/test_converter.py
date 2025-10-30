# tests/test_converter.py
from json2csv import json_files_to_csv
from pathlib import Path
import tempfile, json

def test_converter():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p/"a.json").write_text(json.dumps({"name":"A","age":10}))
        (p/"b.json").write_text(json.dumps([{"name":"B","age":20},{"name":"C"}]))
        out = p/"out.csv"
        json_files_to_csv(p, out)
        assert out.exists()
        text = out.read_text()
        assert "name" in text
